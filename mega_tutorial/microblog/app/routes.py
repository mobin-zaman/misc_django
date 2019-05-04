from app import app
from app.models import User
from flask_login import current_user, login_user
from flask import render_template ,redirect


@app.route('/')
@app.route('/index')
def index():
    return "hello, world"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    from = LoginForm()
    if from.validate_on_submit():
        use
