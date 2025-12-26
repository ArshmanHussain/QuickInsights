# **QuickInsights – Interactive Analytics Dashboard**

**Turn your product data into actionable insights instantly!**

“Turn your product data into actionable insights! Upload your CSV and instantly see top products, revenue by category, and sales trends with interactive charts — a clean, responsive dashboard designed to help businesses make smarter decisions.”

---

## **Why This Dashboard Matters for Your Business**

* **Instant Insights:** Upload your product data and immediately visualize top products, revenue by category, and sales trends.
* **Better Decisions:** See which products perform best and make informed business strategies.
* **Time-Saving:** No Excel or manual calculations — everything updates automatically.
* **Client-Ready Design:** Clean, responsive UI built with Bootstrap, suitable for desktop and mobile.
* **Freelance-Ready:** Modular, easy-to-customize code structure to quickly integrate into client projects.

---

## **Key Features**

* **CSV Upload:** Import your product list (name, category, price, quantity) instantly.
* **Interactive Charts:**

  * **Top Products:** Bar chart for product quantities
  * **Revenue by Category:** Pie chart for category-wise revenue
  * **Sales Over Time:** Line chart (from API or backend data)
* **KPI Cards:** Quick glance at Total Revenue, Total Orders, and Total Products.
* **Responsive Design:** Works perfectly on desktop, tablet, and mobile.

---

## **How It Works**

1. Upload a **CSV file** with your product data.
2. Dashboard automatically calculates **revenue, quantities, and totals**.
3. Charts and KPIs update dynamically without page reload.
4. Sales Over Time chart pulls data from your API/backend.

**CSV format expected:**

| name      | category    | price | quantity |
| --------- | ----------- | ----- | -------- |
| Product A | Electronics | 100   | 5        |
| Product B | Clothing    | 50    | 10       |

---

## **Tech Stack**

* **Backend:** Python, Flask
* **Frontend:** HTML, Bootstrap, JavaScript
* **Charts:** Chart.js
* **Data Handling:** CSV Upload and JSON APIs

---

## **How to Run**

1. Clone the repo:

```bash
git clone https://github.com/ArshmanHussain/QuickInsights.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run Flask app:

```bash
python run.py
```

4. Open your browser at `http://127.0.0.1:5000` and start uploading CSVs.

---
