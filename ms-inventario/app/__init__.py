from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
    db_url    = os.getenv('FIREBASE_DATABASE_URL') #variables globales para firebase

    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': db_url
    })

    # Registrar rutas
    from app.routes.productos import productos_bp
    from app.routes.stock import stock_bp

    app.register_blueprint(productos_bp)
    app.register_blueprint(stock_bp)

    return app