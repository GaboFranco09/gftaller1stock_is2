from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registrar rutas
    from app.routes.productos import productos_bp
    from app.routes.stock import stock_bp

    app.register_blueprint(productos_bp)
    app.register_blueprint(stock_bp)

    return app