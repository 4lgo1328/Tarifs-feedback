from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.routes import *
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_ENABLED'] = True
app.config["SECRET_KEY"] = 'hui'
csrf = CSRFProtect(app)
app.config.from_object(Config)

db.init_app(app)

init_routes(app, db)

if __name__ == "__main__":
    app.run(debug=True)
