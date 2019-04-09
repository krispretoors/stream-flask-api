import os

from flask import jsonify
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

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
    if request.method == 'POST':
        return jsonify(success=True, data=jsonData)

    return 'post method reached'

if __name__ == '__main__':
    app.run()