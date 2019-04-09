import os

from flask import jsonify
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

from models import Student, TestResult

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "hello world"


if __name__ == '__main__':
    app.run()