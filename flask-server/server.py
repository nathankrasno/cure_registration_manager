from flask import Flask
from flask_cors import CORS

import pandas as pd

app = Flask(__name__)
CORS(app)

#Available courses API route
@app.route("/courses")
def courses():

    return {"courses": ["course1", "course2", "course3"]}

if __name__=="__main__":
    app.run(debug=True)