from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# from hello import route_registrator

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2Mr6jS5r@localhost:5432/myprojectdb'
db = SQLAlchemy(app)

from selling.model import QuotesName, Quote

from selling.controller import route_registrator
app.register_blueprint(route_registrator)
