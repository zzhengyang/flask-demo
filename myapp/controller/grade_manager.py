#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from myapp.model.Grade import Grade
from myapp.model.Student import Student
from myapp import app, db

from flask import render_template, flash, request, redirect, url_for

@app.route('/grades/<sorted>')
def allGrade(sorted):
    if sorted == 'byname':
        grades = db.session.query(Grade)\
                                .join(Student, Student.id == Grade.student_id)\
                                .order_by(Student.first_name).all()
    else:
        grades = Grade.query.order_by(Grade.grade.desc()).all()

    for index in range(len(grades)):
        nameQueryer = Student.query.with_entities(Student.first_name, Student.last_name).filter(
            Student.id == grades[index].student_id).first()
        name = nameQueryer[0] + ' ' + nameQueryer[1] if nameQueryer else ''
        grades[index].name = name
    return render_template('grade/index.html', grades=grades)

@app.route('/grade/<sid>')
def queryGrade(sid):
    grades = Grade.query.filter(Grade.student_id == sid).order_by(Grade.grade.desc()).all()
    for index in range(len(grades)):
        nameQueryer = Student.query.with_entities(Student.first_name, Student.last_name).filter(
            Student.id == grades[index].student_id).first()
        name = nameQueryer[0] + ' ' + nameQueryer[1] if nameQueryer else ''
        grades[index].name = name
    return render_template('grade/index.html', grades=grades)

@app.route('/grade/add', methods=['GET', 'POST'])
def addGrade():
    if request.method == 'POST':
        student_id = request.form['student_id']
        assignments_id = request.form['assignments_id']
        grade = request.form['grade']

        grade_record = Grade(student_id, assignments_id, grade)
        db.session.add(grade_record)
        db.session.commit()
        flash('New grade record was successfully added')
        return redirect(url_for('allGrade', sorted='bygrade'))
    return render_template('grade/addgrade.html')


@app.route('/grade/delete/<id>')
def deleteGrade(id):
    grade = Grade.query.filter(Grade.id == id).first()
    db.session.delete(grade)
    db.session.commit()

    flash('Grade record was successfully deleted')
    return redirect(url_for('allGrade'))

@app.route('/grade/update/<sid>')
def updateGrade(sid):
    return sid
