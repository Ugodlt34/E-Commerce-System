from flask import Blueprint, request, jsonify
from models.cart import Cart
from api.user_routes import users
from api.product_routes import products

cart_bp = Blueprint('cart_bp', __name__)

carts = {}

@cart_bp.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.json
    user = users.get(data['username'])
    product = products.get(data['product_id'])
    if user and product:
        cart = carts.setdefault(user.username, Cart(user))
        message = cart.add_product(product, data['quantity'])
        return jsonify({"message": message})
    return jsonify({"message": "User or Product not found."}), 404

@cart_bp.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.json
    user = users.get(data['username'])
    product = products.get(data['product_id'])
    if user and product:
        cart = carts.get(user.username)
        if cart:
            message = cart.remove_product(product)
            return jsonify({"message": message})
    return jsonify({"message": "User, Product, or Cart not found."}), 404
