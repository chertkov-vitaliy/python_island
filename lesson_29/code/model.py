from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:123@localhost:5432/orm'
db.init_app(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    age = db.Column(db.Integer, nullable=False)
    online = db.Column(db.Boolean, nullable=True)
    online_ = db.Column(db.Boolean, nullable=True)
    id_account = db.Column(db.ForeignKey('account.id'))


class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    login = db.Column(db.String)
    password = db.Column(db.String)
    user = db.relationship('User', backref='account')

with app.app_context():
   db.create_all()


