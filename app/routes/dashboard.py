from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import csv
from io import TextIOWrapper

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
@login_required
def index():
    return render_template("dashboard.html", current_user=current_user)

@dashboard_bp.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Read CSV file
        stream = TextIOWrapper(file.stream)
        csv_reader = csv.DictReader(stream)
        products = []

        for row in csv_reader:
            products.append({
                "name": row['name'],
                "category": row['category'],
                "price": float(row['price']),
                "quantity": int(row['quantity'])
            })

        return jsonify(products)  # return JSON to JS

    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to read CSV"}), 400

