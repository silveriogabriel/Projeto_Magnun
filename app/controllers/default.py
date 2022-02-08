from app import app
from flask import render_template

@app.route("/login")
@app.route('/')
def homepage():
    return render_template('login.html')

@app.route('/cadastre-se')
def cadastrese():
    return render_template('cadastro.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)
