from app import db
from datetime import datetime


class User(db.Model):
    # TODO: the jokes field needed to be checked
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(255))
    jokes = db.relationship('Joke', backref='author', lazy='dynamic')
    joined_on = db.Column(db.DateTime, default=datetime.utcnow())

    """this is for showing in console"""


    def __init__(self,username,email,password_hash):
        self.username=username
        self.email=email
        self.password_hash=password_hash

    def __repr__(self):
        return '<User {}>'.format(self.username, self.email)


class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Joke {}>'.format(self.user_id, self.body)
