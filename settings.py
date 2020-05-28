#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class BaseConfig(object):
    TESTING = False
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://dbuser:123456@127.0.0.1:3306/ningbo"

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
            username="liuzh1135",
            password="123456",
            hostname="liuzh1135.mysql.pythonanywhere-services.com",
            databasename="liuzh1135$ningbo",
        )