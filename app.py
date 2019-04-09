import os
import json

from flask import jsonify
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Student, TestResult
from businesslogic import DatabaseCalls

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/marks")
def display_marks():
    return render_template("marks.html")

@app.route("/getdata")
def get_test_data():
    try:
        result = db.engine.execute("SELECT COUNT(DISTINCT test) FROM testresults;")
        print(result)
        tests = User.query.order_by(tests='test').all()
        return  jsonify([e.serialize() for e in books])
    except Exception as e:
	    return(str(e))

@app.route("/data/persist",methods=['POST'])
def payload_handler():
    jsonData = request.get_json()
    buslogic = DatabaseCalls(jsonData)
    if request.method == 'POST':
        is_persisted = buslogic.persist_data_to_db(jsonData)
        if is_persisted:
            return jsonify(success=True, data=jsonData)
        else:
            return jsonify(success=False)

if __name__ == '__main__':
    app.run()