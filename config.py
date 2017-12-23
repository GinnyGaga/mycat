#!/usr/bin/env python
# -- coding:utf-8--

import os
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

SECRET_KEY = os.urandom(24)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
USERNAME = 'root'
PASSWORD = 'root'
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'mycat_demo'
SQLALCHEMY_DATABASE_URI = DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,
                                        PASSWORD,HOSTNAME ,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False




