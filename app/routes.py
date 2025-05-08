from flask import render_template
from app import app,db
from app.models import Student

from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Student
from app.forms import StudentForm  # Importez votre formulaire


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students/<int:student_id>')
def student_details(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('students/student.html', student=student)

@app.route('/students')
def list_students():
    students = Student.query.all()
    return render_template('students/list.html', students=students)


@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(first_name=form.first_name.data,
                          last_name=form.last_name.data,
                          id=form.id.data,
                          email=form.email.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('list_students'))
    return render_template('students/add.html', title='Ajouter un étudiant', form=form)

from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Student
from app.forms import StudentForm

@app.route('/students/<int:student_id>/edit', methods=['GET', 'POST'])
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.first_name = form.first_name.data
        student.last_name = form.last_name.data
        student.email = form.email.data
        # ... mettre à jour les autres champs ...
        db.session.commit()
        return redirect(url_for('list_students'))
    return render_template('students/edit.html', title='Modifier un étudiant', form=form, student=student)