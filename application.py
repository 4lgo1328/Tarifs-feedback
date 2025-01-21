from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.routes import *
from flask_wtf.csrf import CSRFProtect
from app.models import db


def run_app():
    app = Flask(__name__)

    csrf = CSRFProtect(app)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    init_routes(app, db)

    app.run(debug=True)

