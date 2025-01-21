from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.routes import *
from flask_wtf.csrf import CSRFProtect
from app.models import db
from bot import parse_updates
from threading import Thread


def run_app():
    app = Flask(__name__)

    csrf = CSRFProtect(app)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    init_routes(app, db)

    app.run(debug=True, use_reloader=False)


if __name__ == "__main__":
    app_thread, bot_thread = Thread(target=run_app), Thread(target=parse_updates)
    app_thread.start(), bot_thread.start()
    app_thread.join(), bot_thread.join()
