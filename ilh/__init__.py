from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'gachimuchi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kibee:1234@localhost:3306/first_flask'
db = SQLAlchemy(app)
manager = LoginManager(app)


from ilh import models, routes

db.create_all()
