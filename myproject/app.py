from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from hello import route_registrator
from selling.controller import route_registrator

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

app.register_blueprint(route_registrator)
