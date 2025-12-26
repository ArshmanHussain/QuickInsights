from app.extensions import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)

    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id"), nullable=False
    )

    category = db.relationship("Category", back_populates="products")
    order_items = db.relationship("OrderItem", back_populates="product")

    def __repr__(self):
        return f"<Product {self.name}>"
