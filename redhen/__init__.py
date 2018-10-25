from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '49e2cb64b943de1604bc654097c6a261'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///redhen.db'
db = SQLAlchemy(app)

from redhen import routes