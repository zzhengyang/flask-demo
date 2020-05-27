#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：stuManager -> settings
@IDE    ：PyCharm
@Author ：zhengy
@Date   ：2020/5/27 2:36 PM
@Desc   ：
=================================================='''

class BaseConfig(object):
    TESTING = False
    FILE_NAME = 'students.txt'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://dbuser:123456@127.0.0.1:3306/ningbo"

class ProductionConfig(BaseConfig):
    DATABASE_URI = 'mysql+pymysql://dbuser:123456@127.0.0.1:3306/ningbo'