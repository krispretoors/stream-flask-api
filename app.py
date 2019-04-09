import os

from flask import jsonify
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"


if __name__ == '__main__':
    app.run()