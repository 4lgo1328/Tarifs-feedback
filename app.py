from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.routes import *

# Initialize extensions
db = SQLAlchemy()


app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_ENABLED'] = True

app.config.from_object(Config)
app.config["SECRET_KEY"] = 'hui'

db.init_app(app)

init_routes(app, db)

if __name__ == "__main__":
    app.run(debug=True)
