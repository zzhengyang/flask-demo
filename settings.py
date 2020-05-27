#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class BaseConfig(object):
    TESTING = False
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://dbuser:123456@127.0.0.1:3306/ningbo"

class ProductionConfig(BaseConfig):
    DATABASE_URI = 'mysql+pymysql://dbuser:123456@127.0.0.1:3306/ningbo'