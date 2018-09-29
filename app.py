import os

from flask import Flask, jsonify, redirect, render_template, request, url_for
import psycopg2

import db

app = Flask(__name__)

@app.before_first_request
def initialize():
    db.setup()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/survey")
def survey():
        return render_template("survey.html")

@app.route("/decline")
def decline():
            return render_template("decline.html")

@app.route("/thanks")
def thanks():
            return render_template("thanks.html")

#TODO This entire method needs to be changed
@app.route('/api/foo')
def api_foo():
    data = {
        "message": "hello, world",
        "isAGoodExample": False,
        "aList": [1, 2, 3],
        "nested": {
            "key": "value"
        }
    }
    return jsonify(data)


if __name__ == "__main__":
            app.run(debug=True)
