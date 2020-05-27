#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from myapp import db

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    major = db.Column(db.String(50))
    email = db.Column(db.String(40))
    class_id = db.Column(db.Integer)
    gpa = 0.0

    def __init__(self, first_name, last_name, major, email, class_id):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.email = email
        self.class_id = class_id

    def __repr__(self):
        return '<Student %r>' % self.id