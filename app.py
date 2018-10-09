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

        if (q5 == "No."):
            with db.get_db_cursor(commit=True) as cur:
                cur.execute("insert into survey (q1, q2, q3, q4, q5) values (%s, %s, %s, %s, %s)", (q1, q2, q3, q4, q5,))

        else:
            q6 = request.form['q6']
            app.logger.info(f"q6: {q6}")

            with db.get_db_cursor(commit=True) as cur:
                cur.execute("insert into survey (q1, q2, q3, q4, q5, q6) values (%s, %s, %s, %s, %s, %s)", (q1, q2, q3, q4, q5, q6,))

        return redirect(url_for("thanks"))
    else:
        return render_template("thanks.html")

@app.route('/admin/summary')
def admin_summary():

    with db.get_db_cursor(commit=True) as cur:
        query1 = "SELECT S.q1 FROM survey S"
        cur.execute(query1)
        q1 = cur.fetchall()

        query2 = "SELECT COUNT(*), S.q2 FROM survey S GROUP BY S.q2"
        cur.execute(query2)
        q2 = cur.fetchall()

        query3 = "SELECT COUNT(*), S.q3 FROM survey S GROUP BY S.q3"
        cur.execute(query3)
        q3 = cur.fetchall()

        query4 = "SELECT COUNT(*), S.q4 FROM survey S GROUP BY S.q4"
        cur.execute(query4)
        q4 = cur.fetchall()

        query5 = "SELECT COUNT(*), S.q5 FROM survey S GROUP BY S.q5"
        cur.execute(query5)
        q5 = cur.fetchall()

        #TODO insert a condition where you don't send q6 if q5 is No
        query6 = "SELECT COUNT(*), S.q6 FROM survey S GROUP BY S.q6"
        cur.execute(query6)
        q6 = cur.fetchall()

        app.logger.info(f"Q1: {q1}")
        app.logger.info(f"Q2: {q2}")
        app.logger.info(f"Q3: {q3}")
        app.logger.info(f"Q4: {q4}")
        app.logger.info(f"Q5: {q5}")
        app.logger.info(f"Q6: {q6}")


    return render_template("summary.html", q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6)

@app.route('/api/results')
def api_results():

    reverse = request.args.get('reverse')

    with db.get_db_cursor(commit=True) as cur:
        query = "SELECT * FROM survey"
        cur.execute(query)
        result = cur.fetchall()
        items = []

        app.logger.info(f"Reverse is {reverse}")
        if(reverse == 'true'):
            app.logger.info(f"In the reverse")
            for row in reversed(result):
                i = 0
                for key in cur.description:
                    items.append({key[0]: row[i]})
                    i = i + 1

        else:
            app.logger.info(f"In normal")
            for row in result:
                i = 0
                for key in cur.description:
                    items.append({key[0]: row[i]})
                    i = i + 1


        return jsonify({'Responses': items})


if __name__ == "__main__":
            pass
            #app.run(debug=True)
