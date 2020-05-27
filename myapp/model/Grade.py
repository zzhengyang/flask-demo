#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from myapp import db

class Grade(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer)
    assignments_id = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    name = ''

    def __init__(self, student_id, assignments_id, grade):
        self.student_id = student_id
        self.assignments_id = assignments_id
        self.grade = grade
        self.name = ''

    def __repr__(self):
        return '<Grade %r>' % self.id