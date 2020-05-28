#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# from flask.ext.login import login_required, login_user, logout_user

from myapp.model.Student import Student
from myapp.model.Grade import Grade
from myapp import app, db

from flask import request,render_template,flash,url_for,redirect

@app.route('/')
def index():
    students = Student.query.all()
    for loop_index in range(len(students)):
        gradeInfo = db.session.execute("select count(*), sum(`grade`) \
                            from grade where student_id=%s" % (students[loop_index].id)).first()
        if gradeInfo[0] > 0:
            students[loop_index].gpa = round(gradeInfo[1] / gradeInfo[0], 2)

    return render_template('students/index.html', students=students)


@app.route('/stu/delete/<id>')
def deleteStudent(id):
    student = Student.query.filter(Student.id == id).first()
    grades = Grade.query.filter(Grade.student_id == id).delete()
    db.session.delete(student)
    db.session.commit()
    flash('Student and his grades was successfully deleted')
    return redirect(url_for('index'))


@app.route('/stu/add', methods=['GET', 'POST'])
def addStudent():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        major = request.form['major']
        email = request.form['email']
        class_id = request.form['class_id']

        student = Student(first_name, last_name, major, email, class_id)
        db.session.add(student)
        db.session.commit()
        flash('New student was successfully added')
        return redirect(url_for('index'))
    return render_template('students/addstu.html')


@app.route('/stu/update/<id>', methods=['GET', 'POST'])
def updateStudent(id):
    student = Student.query.filter(Student.id == id).first()
    if request.method=='POST':
        student.first_name = request.form['first_name']
        student.last_name = request.form['last_name']
        student.major = request.form['major']
        student.email = request.form['email']
        student.class_id = request.form['class_id']
        db.session.commit()
        flash("Student's information was successfully updated")
        return redirect(url_for('index'))

    return render_template('students/altstu.html', student=student)
