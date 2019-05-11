from flask import Flask, g
# this below line should be app.config, putting only config doesn't work
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)


# Ensure a separate connection for each thread
# @app.before_request
# def before_request():
#     g.db = db
#     g.db.connect()
#
#
# @app.after_request
# def after_request(response):
#     g.db.close()
#     return response


from app import resource, model
