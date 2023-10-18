from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/alberta", methods=["GET", "POST"])
def alberta():
    return render_template("alberta.html")


@app.route("/bc", methods=["GET", "POST"])
def bc():
    return render_template("bc.html")


@app.route("/manitoba", methods=["GET", "POST"])
def manitoba():
    return render_template("manitoba.html")


@app.route("/newbrunswick", methods=["GET", "POST"])
def newbrunswick():
    return render_template("newbrunswick.html")


@app.route("/nf", methods=["GET", "POST"])
def nf():
    return render_template("nf.html")


@app.route("/nwt", methods=["GET", "POST"])
def nwt():
    return render_template("nwt.html")


@app.route("/ns", methods=["GET", "POST"])
def ns():
    return render_template("ns.html")


@app.route("/nunavut", methods=["GET", "POST"])
def nunavut():
    return render_template("nunavut.html")


@app.route("/ontario", methods=["GET", "POST"])
def ontario():
    return render_template("ontario.html")


@app.route("/pei", methods=["GET", "POST"])
def pei():
    return render_template("pei.html")


@app.route("/quebec", methods=["GET", "POST"])
def quebec():
    return render_template("quebec.html")


@app.route("/saskatchewan", methods=["GET", "POST"])
def saskatchewan():
    return render_template("saskatchewan.html")


@app.route("/yukon", methods=["GET", "POST"])
def yukon():
    return render_template("yukon.html")


@app.route("/country", methods=["GET", "POST"])
def country():
    return render_template("country.html")


if __name__ == "__main__":
    app.run(debug=True)
