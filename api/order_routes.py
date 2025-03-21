from flask import Blueprint, request, jsonify
from models.order import Order
from models.cart import Cart
from api.user_routes import users
from api.cart_routes import carts

order_bp = Blueprint('order_bp', __name__)

orders = {}
order_counter = 1

@order_bp.route('/orders/place', methods=['POST'])
def place_order():
    global order_counter
    data = request.json
    user = users.get(data['username'])
    cart = carts.get(user.username)
    if user and cart:
        order = Order(order_counter, user, cart.items)
        message = order.place_order()
        orders[order_counter] = order
        order_counter += 1
        carts[user.username] = Cart(user)  # Reset cart
        return jsonify({"message": message, "order_id": order.order_id})
    return jsonify({"message": "User or Cart not found."}), 404

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        items = [product.product_name for product, _ in order.items.values()]
        return jsonify({"order_id": order.order_id, "items": items, "status": order.status})
    return jsonify({"message": "Order not found."}), 404