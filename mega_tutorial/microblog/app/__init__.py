from flask import Flask
#this below line should be app.config, putting only config doesn't work
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate =  Migrate(app,db)
login = LoginManager(app)

from app import routes,models