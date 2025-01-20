from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    pic_filename = db.Column(db.String(100), nullable=False)
    db.Column(db.DateTime, default=datetime.utcnow)
    feedback_text = db.Column(db.String(1000), nullable=False, unique=True)

    def __repr__(self):
        return f'<User {self.username}>'

