from flask_sqlalchemy import SQLAlchemy
import datetime
from redhen import db

class Comic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    pages = db.relationship('Page', backref='comic', lazy=True)

    def __repr__(self):
        return self.title


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comic_id = db.Column(db.Integer, db.ForeignKey('comic.id'), nullable=False)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)