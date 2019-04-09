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

if __name__ == '__main__':
    app.run()