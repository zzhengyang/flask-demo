#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# load config file
app.config.from_object('settings.BaseConfig')

db = SQLAlchemy(app)

from myapp.controller import student_manager
from myapp.controller import grade_manager


