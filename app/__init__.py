from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#Definindo flask

app = Flask(__name__)
app.config.from_object('settings')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import default
from app.models import tables