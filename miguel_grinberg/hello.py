import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    user_agent = request.headers.get('User-agent')
    return '<p> Your browser is %s</p>' % user_agent


@app.route('/index')
def user(name):
    return render_template('index.html')


@app.route('/user/<name>')
def user(name)eturn render_template('user.html', name=name)


@app.route('/demo')
def make_cookie():
    response = make_response('<h1> this document carries a cookie!</h1>')
    response.set_cookie('answer', 42)
    return response


@app.route('/redirect')
def redirection():
    return redirect('http://example.com')


# @app.rout('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1> Hello, %s</h1>' % user.name
if __name__ == '__main__':
    app.run()
