from app import app
from flask import render_template

@app.route("/index/<user>")
@app.route("/")
def homepage(user = None):
    return render_template('index.html', user = user)

@app.route("/login")
def pagina_login():
    return render_template('login.html')

@app.route('/cadastre-se')
def pagina_cadastro():
    return render_template('cadastro.html')

