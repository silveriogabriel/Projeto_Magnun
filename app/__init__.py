from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#Definindo flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import default

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))