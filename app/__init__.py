from flask import Flask, render_template

#Definindo flask

app = Flask(__name__)

from app.controllers import default

