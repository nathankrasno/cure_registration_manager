from flask import Flask
from flask_cors import CORS
import sqlite3
import datetime
from courses import populateCourses

DATABASE = ''

app = Flask(__name__)
CORS(app)

#Available courses API route
@app.route("/courses")
def courses():
    return populateCourses()

@app.route('/time')
def get_current_time():
    return {'time:': datetime.datetime.now()}

if __name__=="__main__":
    app.run(debug=True)