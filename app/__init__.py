#!/usr/bin/env python
# -- coding:utf-8--

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

