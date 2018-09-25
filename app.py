
from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
            app.run(debug=True)
