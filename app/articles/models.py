from app.extensions.database import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # article = db.relationship("Article", backref="user", uselist=False, lazy=True)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(20), unique=True)
    title = db.Column(db.String(80))
    text = db.Column(db.Text())
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
