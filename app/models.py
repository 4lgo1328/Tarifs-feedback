from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(100), nullable=False)
    db.Column(db.DateTime, default=datetime.now)
    feedback = db.Column(db.String(1000), nullable=False)


