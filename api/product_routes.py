from flask import Blueprint, request, jsonify
from models.product import Product

product_bp = Blueprint('product_bp', __name__)

products = {}

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    product = Product(data['product_name'], data['product_id'], data['price'], data['stock_quantity'])
    products[data['product_id']] = product
    return jsonify({"message": "Product added."})

@product_bp.route('/products', methods=['GET'])
def list_products():
    result = [product.get_product_details() for product in products.values()]
    return jsonify({"products": result})

@product_bp.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify({"details": product.get_product_details()})
    return jsonify({"message": "Product not found."}), 404
