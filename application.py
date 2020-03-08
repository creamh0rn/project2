import os
import flask
import requests

from flask import Flask, render_template, session, redirect, url_for, request, jsonify
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


        #define a topics variable
        #should this be outside this function?

        if session.get("topic_names") == None:
            topic_names = []
            topic_names.append(2)
            session['topic_names'] = topic_names
        else:
            topic_names = session.get('topic_names')
            topic_names.append(5)
            session['topic_names'] = topic_names


        topic_names = ["CARROT", "CAKE"]
        return render_template("home.html", user_name = session['user_name'], topic_names = topic_names)






@app.route("/topics", methods=["POST"])
def topics():

    # Get start and end point for posts to generate.
    start = 1
    end = 11

    # Generate list of posts.
    data = []
    for i in range(start, end + 1):
        data.append("cake")


    # Return list of posts.
    return jsonify(data)







@app.route('/sign_out', methods=["POST"])
def sign_out():
    # remove the username from the session if it's there
    session.pop('user_name', None)
    return redirect(url_for('sign_in'))



if __name__ == "__main__":
    socketio.run(app)
