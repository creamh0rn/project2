import os
import flask
import requests

from flask import Flask, render_template, session, redirect, url_for, request
from flask_socketio import SocketIO, emit
from flask_session import Session


app = Flask(__name__)
app.secret_key = 'captainramma'
socketio = SocketIO(app)

@app.route("/", methods=["GET"])
def index():
    if session.get("user_name") == None:
        return redirect(url_for("sign_in"))
    else:
        return redirect(url_for('home'))

@app.route("/sign_in", methods=["GET"])
def sign_in():

    return render_template("sign_in.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if flask.request.method == "GET":
        if session.get("user_name") == None:
            return redirect(url_for("sign_in"))
        else:

            return render_template("home.html", user_name = session['user_name'])
    else:
        user_name = request.form.get("user_name")
        session['user_name'] = user_name
        return render_template("home.html", user_name = user_name)



if __name__ == "__main__":
    socketio.run(app)
