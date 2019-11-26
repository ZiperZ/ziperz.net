from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = b'c\x8a \xac\xdcf\xae\x84\x03w\x9e\x06\xad\x12D^+\x80\x98\x16\x0e\xa1?\xc9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ziperz.db'
db = SQLAlchemy(app)

from ziperz import pages