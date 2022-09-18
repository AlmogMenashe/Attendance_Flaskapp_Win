#!/usr/bin/python

from msilib.schema import tables
from flask import Flask, redirect, url_for, render_template
from flask_remote_file import RemoteFile
import runAttendance

app = Flask(__name__)
df = runAttendance.df3

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/attentdance")
def attentdance():
    return render_template("attentdance.html",  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

#app.run(host='0.0.0.0', port=81)

if __name__ == '__main__':
    app.run(debug=True)
