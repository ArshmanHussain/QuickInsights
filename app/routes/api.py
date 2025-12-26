from flask import Blueprint, jsonify, render_template
from sqlalchemy import func
from app.extensions import db
from app.models import Order, OrderItem, Product, Category
from flask import request, send_file
import csv
import io
from datetime import datetime

api_bp = Blueprint("api", __name__)

products = []
product_id = 1

@api_bp.route("/")
def dashboard():
    return render_template("dashboard.html", products=products)


@api_bp.route('/products')
def get_products():
    return jsonify(products)


    products.append(product)
    product_id += 1
    return jsonify(products)

@api_bp.route("/upload-csv", methods=["POST"])
def upload_csv():
    global product_id
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]

    stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    reader = csv.DictReader(stream)

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400


    import csv, io
    stream = io.StringIO(file.stream.read().decode("utf-8"))
    reader = csv.DictReader(stream)

    for row in reader:
        products.append({
            "id": product_id,
            "name": row["name"],
            "category": row["category"],
            "price": float(row["price"]),
            "quantity": int(row["quantity"])
        })
        product_id += 1

    return jsonify(products)


@api_bp.route("/orders")
def get_orders():
    order_id = request.args.get("order_id")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    query = Order.query
    if order_id:
        query = query.filter(Order.id == int(order_id))
    if start_date:
        query = query.filter(Order.order_date >= datetime.fromisoformat(start_date))
    if end_date:
        query = query.filter(Order.order_date <= datetime.fromisoformat(end_date))

    orders = query.order_by(Order.order_date.desc()).all()
    data = [{"id": o.id, "date": o.order_date.strftime("%Y-%m-%d %H:%M"), "total_amount": float(o.total_amount)} for o in orders]
    return {"orders": data}

@api_bp.route("/orders/export")
def export_orders_csv():
    orders = Order.query.order_by(Order.order_date.desc()).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Order ID", "Date", "Total Amount"])
    for o in orders:
        writer.writerow([o.id, o.order_date.strftime("%Y-%m-%d %H:%M"), float(o.total_amount)])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype="text/csv", download_name="orders.csv", as_attachment=True)

@api_bp.route("/sales-over-time")
def sales_over_time():
    results = (
        db.session.query(
            func.date_format(Order.order_date, "%Y-%m").label("month"),
            func.sum(Order.total_amount).label("revenue")
        )
        .group_by("month")
        .order_by("month")
        .all()
    )

    labels = [row.month for row in results]
    values = [float(row.revenue) for row in results]

    return jsonify({
        "labels": labels,
        "values": values
    })

@api_bp.route("/revenue-by-category")
def revenue_by_category():
    results = (
        db.session.query(
            Category.name.label("category"),
            func.sum(OrderItem.quantity * OrderItem.price).label("revenue")
        )
        .join(Product, Product.id == OrderItem.product_id)
        .join(Category, Category.id == Product.category_id)
        .group_by(Category.name)
        .order_by(func.sum(OrderItem.quantity * OrderItem.price).desc())
        .all()
    )

    labels = [row.category for row in results]
    values = [float(row.revenue) for row in results]

    return jsonify({
        "labels": labels,
        "values": values
    })

@api_bp.route("/top-products")
def top_products():
    results = (
        db.session.query(
            Product.name.label("product"),
            func.sum(OrderItem.quantity).label("total_sold")
        )
        .join(OrderItem, Product.id == OrderItem.product_id)
        .group_by(Product.name)
        .order_by(func.sum(OrderItem.quantity).desc())
        .limit(5)
        .all()
    )

    labels = [row.product for row in results]
    values = [int(row.total_sold) for row in results]

    return jsonify({
        "labels": labels,
        "values": values
    })
