from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(80), nullable=False)
    last_name=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<Student %r>' % self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"