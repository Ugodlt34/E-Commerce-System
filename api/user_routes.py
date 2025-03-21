from flask import Blueprint, request, jsonify
from models.user import User

user_bp = Blueprint('user_bp', __name__)

users = {}

@user_bp.route('/users/register', methods=['POST'])
def register_user():
    data = request.json
    user = User(data['username'], data['email'], data['password'])
    users[data['username']] = user
    return jsonify({"message": user.register()})

@user_bp.route('/users/login', methods=['POST'])
def login_user():
    data = request.json
    user = users.get(data['username'])
    if user and user.login(data['password']):
        return jsonify({"message": "Login successful."})
    return jsonify({"message": "Invalid credentials."}), 401

@user_bp.route('/users/<username>/orders', methods=['GET'])
def get_order_history(username):
    user = users.get(username)
    if user:
        history = [order.order_id for order in user.view_order_history()]
        return jsonify({"order_history": history})
    return jsonify({"message": "User not found."}), 404
