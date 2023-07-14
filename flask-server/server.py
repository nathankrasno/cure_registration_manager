from flask import Flask
from flask_cors import CORS
import sqlite3
import datetime
from courses import populateCourses
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#Available courses API route
@app.route("/courses")
def courses():
    return populateCourses()

@app.route('/time')
def get_current_time():
    return {'time:': datetime.datetime.now()}

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(50))
    last = db.Column(db.String(50))
    email = db.Column(db.String(50))
    major = db.Column(db.String(50))
    choice1 = db.Column(db.String(50))
    choice2 = db.Column(db.String(50))
    choice3 = db.Column(db.String(50))
    courseAssignment = db.Column(db.String(50))

    def __repr__(self):
        return f"<Student {self.first} {self.last}>"


if __name__=="__main__":
    app.run(debug=True)