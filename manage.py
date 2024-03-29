#!/usr/bin/env python
# -- coding:utf-8--

from flask import Flask
from app import db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()
