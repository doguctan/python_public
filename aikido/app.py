'''
!pip install Flask
!pip install Flask-SQLAlchemy
!pip install Flask-WTF
'''

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField

#from wtforms.fields.html5 import MultipleSelectField

from wtforms import Form, SelectMultipleField

from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Technique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tech_name = db.Column(db.String, nullable=False)
    # Create the Technique table in the database
with app.app_context():
    Technique.metadata.create_all(db.engine)

class AikiClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    technique1 = db.Column(db.String)
    technique2 = db.Column(db.String)
    technique3 = db.Column(db.String)
    technique4 = db.Column(db.String)
    technique5 = db.Column(db.String)
    technique6 = db.Column(db.String)
    technique7 = db.Column(db.String)
    technique8 = db.Column(db.String)
    technique9 = db.Column(db.String)
    technique10 = db.Column(db.String)
with app.app_context():
    AikiClass.metadata.create_all(db.engine)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    dateofbirth = db.Column(db.Date, nullable=False)
    register_date = db.Column(db.Date, nullable=False)
with app.app_context():
    Student.metadata.create_all(db.engine)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    student_name = db.Column(db.String, nullable=False)
    student_surname = db.Column(db.String, nullable=False)
    aikido_technique = db.Column(db.String, nullable=False)

with app.app_context():
    Attendance.metadata.create_all(db.engine)

class NewStudentForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    surname = StringField('Surname', validators=[InputRequired()])
    dateofbirth = DateField('Date of Birth', validators=[InputRequired()])
    register_date = DateField('Registration Date', validators=[InputRequired()])


class CreateAikiClassForm(FlaskForm):
    date = DateField('Date', validators=[InputRequired()])
    #techniques = SelectMultipleField('Techniques', choices=[(tech.tech_name, tech.tech_name) for tech in Technique.query.all()], validators=[InputRequired()])
    with app.app_context():
        techniques = SelectMultipleField('Techniques', choices=[(tech.tech_name, tech.tech_name) for tech in Technique.query.all()])

class AddStudentForm(FlaskForm):
    with app.app_context():
        aiki_class = SelectField('Aiki Class', choices=[(ac.date, ac.date) for ac in AikiClass.query.all()], validators=[InputRequired()])
    #students = SelectMultipleField('Students', choices=[(student.name, student.surname) for student in Student.query.all()], validators=[InputRequired()])
    with app.app_context():
        students = SelectMultipleField('Students', choices=[(student.name, student.surname) for student in Student.query.all()])



@app.route("/")
def index():
    return render_template("index.html")


@app.route('/new_student', methods=['GET', 'POST'])
def new_student():
    form = NewStudentForm()

    if form.validate_on_submit():
        student = Student(name=form.name.data,
                         surname=form.surname.data,
                         dateofbirth=form.dateofbirth.data,
                         register_date=form.register_date.data)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('new_student'))

    return render_template('new_student.html', form=form)


@app.route('/create_class', methods=['GET', 'POST'])
def create_class():
    form = CreateAikiClassForm()

    if form.validate_on_submit():
        aiki_class = AikiClass(date=form.date.data,
                               technique1=form.techniques.data[0],
                               technique2=form.techniques.data[1],
                               technique3=form.techniques.data[2],
                               technique4=form.techniques.data[3],
                               technique5=form.techniques.data[4],
                               technique6=form.techniques.data[5],
                               technique7=form.techniques.data[6],
                               technique8=form.techniques.data[7],
                               technique9=form.techniques.data[8],
                               technique10=form.techniques.data[9])
        db.session.add(aiki_class)
        db.session.commit()

        return redirect(url_for('create_class'))

    return render_template('create_class.html', form=form)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = AddStudentForm()

    if form.validate_on_submit():
        aiki_class = AikiClass.query.filter_by(date=form.aiki_class.data).first()
        for student in form.students.data:
            attendance = Attendance(date=aiki_class.date,
                                    student_name=student.name,
                                    student_surname=student.surname,
                                    aikido_technique=aiki_class.technique1)
            db.session.add(attendance)
            if aiki_class.technique2:
                attendance = Attendance(date=aiki_class.date,
                                        student_name=student.name,
                                        student_surname=student.surname,
                                        aikido_technique=aiki_class.technique2)
                db.session.add(attendance)
            if aiki_class.technique3:
                attendance = Attendance(date=aiki_class.date,
                                        student_name=student.name,
                                        student_surname=student.surname,
                                        aikido_technique=aiki_class.technique3)
                db.session.add(attendance)
            if aiki_class.technique4:
                attendance = Attendance(date=aiki_class.date,
                                        student_name=student.name,
                                        student_surname=student.surname,
                                        aikido_technique=aiki_class.technique4)
                db.session.add(attendance)
            if aiki_class.technique5:
                attendance = Attendance(date=aiki_class.date,
                                        student_name=student.name,
                                        student_surname=student.surname,
                                        aikido_technique=aiki_class.technique5)
                db.session.add(attendance)
            if aiki_class.technique6:
                attendance = Attendance(date=aiki_class.date,
                                        student_name=student.name,
                                        student_surname=student.surname,
                                        aikido_technique=aiki_class.technique6)
                db.session.add(attendance)
            if aiki_class.technique6:
                attendance = Attendance(date=aiki_class.date,
                                        student_name=student.name,
                                        student_surname=student.surname,
                                        aikido_technique=aiki_class.technique6)
                db.session.add(attendance)
            if aiki_class.technique6:
                attendance = Attendance(date=aiki_class.date,
                                        student_name=student.name,
                                        student_surname=student.surname,
                                        aikido_technique=aiki_class.technique6)
                db.session.add(attendance)
            if aiki_class.technique6:
                attendance = Attendance(date=aiki_class.date,
                                        student_name=student.name,
                                        student_surname=student.surname,
                                        aikido_technique=aiki_class.technique6)
                db.session.add(attendance)
            if aiki_class.technique6:
                attendance = Attendance(date=aiki_class.date,
                                        student_name=student.name,
                                        student_surname=student.surname,
                                        aikido_technique=aiki_class.technique6)
                db.session.add(attendance)
        db.session.commit()
        return redirect(url_for('add_student'))
    return render_template('add_student.html', form=form)


if __name__ == '__main__':
    #db.create_all()

    # add some initial data
    with app.app_context():
        db.session.add(Technique(tech_name='Irimi-nage'))
        db.session.add(Technique(tech_name='Kokyu-nage'))
        db.session.add(Technique(tech_name='Koshinage'))
        db.session.add(Technique(tech_name='Shihonage'))
        db.session.add(Technique(tech_name='Sokumen-iriminage'))
        db.session.add(Technique(tech_name='Sumiotoshi'))
        db.session.add(Technique(tech_name='Tenchinage'))
        db.session.add(Technique(tech_name='Ude-garami'))
        db.session.add(Technique(tech_name='Udekimenage'))
        db.session.add(Technique(tech_name='Ushiro-iriminage'))
        db.session.commit()

    app.run(debug=True)
