import os

from flask import jsonify
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from 

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Student, TestResult

@app.route("/")
def hello():
    return "hello world"

@app.route("/data/persist",methods=['POST','GET'])
def persist_data_to_db():
    jsonData = request.get_json()

    student_list = jsonData['students']

    for student in student_list:
        test_list = student['tests']
        student = Student(
            name = student['firstName'],
            surname = student['lastName']
        )
        db.session.add(student)
        db.session.commit()

        print(student.id)
        for key, value in test_list.items():
            student_test = TestResult(
                test = key,
                result = value,
                student_id = student.id
            )
            db.session.add(student_test)
            db.session.commit()

    return jsonify(success=True, data=jsonData)
    
if __name__ == '__main__':
    app.run()