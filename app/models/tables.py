from tracemalloc import stop
from app import db
from app.controllers import default

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Coloumn(db.Integer, primary_key=True)
    banca_inicial = db.coloumn(db.Float, default=0)
    stopgain = db.coloumn(db.Integer, defalt=0)
    stoploss = db.coloumn(db.Integer, defalt=0)
    banca_atual = db.coloumn(db.Float, default=0)
    green = db.coloumn(db.Float, default=0)
    red = db.coloumn(db.Float, default=0)
    primeira_entrada = db.coloumn(db.Float, default=0)
    user_id = db.column(db.Text,db.Foreignkey('users.id'))
    created = db.coloumn(db.DateTime)
    rendimento = db.coloumn(db.Float, default=0)

    User = db.relationship('User', foreing_keys=user_id)

    def __init__(self, banca_inicial, stopgain, stoploss, banca_atual, green, red, primeira_entrada, user_id, created, rendimento):
        self.banca_inicial = banca_inicial
        self.banca_atual = banca_atual
        self.stopgain = stopgain
        self.stoploss = stoploss
        self.green = green
        self.red = red
        self.primeira_entrada = primeira_entrada
        self.user_id = user_id
        self.created = created
        self.rendimento = rendimento

    def __repr__(self):
        return f"<Post {self.id}>"
    
