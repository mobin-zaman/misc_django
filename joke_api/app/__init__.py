from flask import Flask
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

from app import resource, model
