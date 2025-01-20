from flask import Flask
from app.routes import *
from app.models import db

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)