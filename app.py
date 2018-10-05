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

@app.route("/survey", methods=['GET', 'POST'])
def survey():
        return render_template("survey.html")

@app.route("/decline")
def decline():
            return render_template("decline.html")

@app.route("/thanks", methods=['GET', 'POST'])
def thanks():
    if request.method == 'POST':
        q1 = request.form['q1']
        app.logger.info(f"q1: {q1}")
        q2 = request.form['q2']
        app.logger.info(f"q2: {q2}")
        q3 = request.form['q3']
        app.logger.info(f"q3: {q3}")
        q4 = request.form['q4']
        app.logger.info(f"q4: {q4}")
        q5 = request.form['q5']
        app.logger.info(f"q5: {q5}")

        with db.get_db_cursor(commit=True) as cur:
            cur.execute("insert into survey (q1, q2, q3, q4, q5) values (%s, %s, %s, %s, %s)", (q1, q2, q3, q4, q5,))

        app.logger.info("Does it make it here")
        return redirect(url_for("thanks"))
    else:
        return render_template("thanks.html")


#TODO This entire method needs to be changed
@app.route('/api/results')
def api_results():
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
            pass
            #app.run(debug=True)
