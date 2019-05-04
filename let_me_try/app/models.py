from app import db

class Joke(db.Model):
    __tablename__='joke'
    id=db.Column(db.Integer,primary_key=True)
    joke_body=db.Column(db.Text,unique=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id,',ondelete='CASCADE'))

    def __repr__(self):
        return '<Joke {}>'.format(self.joke_body)


class User():
    __tablename__='joke'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(60),unique=True)
    password_hash=db.Column(db.String(128))
    jokes = db.relationship('Joke',backref='author',lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)



"""will be used later to identify if the joke was posted before"""
def joke_exists():
    pass