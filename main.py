from flask import Flask
from api.user_routes import user_bp
from api.product_routes import product_bp
from api.cart_routes import cart_bp
from api.order_routes import order_bp

app = Flask(__name__)
