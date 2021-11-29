from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/jobs")
def jobs():
    return render_template("jobs.html")


@app.route("/bases")
def bases():
    return render_template("bases.html")


if __name__ == "__main__":
    app.run(debug=True)
