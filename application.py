import os
import flask
import requests

from flask import Flask, render_template, session, redirect, url_for, request, jsonify, json
from flask_socketio import SocketIO, emit
from flask_session import Session


app = Flask(__name__)
app.secret_key = 'captainramma'
socketio = SocketIO(app)


votes = {"yes": 0, "no": 0, "maybe": 0}



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
            return render_template("home.html", user_name = session['user_name'], votes=votes)
    else:
        user_name = request.form.get("user_name")
        session['user_name'] = user_name


        return render_template("home.html", user_name = session['user_name'], votes=votes)


@app.route("/add_new_chat", methods=["POST"])
def add_new_chat():

    topic = "cakes"
    content = "hello"
    sent_by = "christoper"
    sent_time = "now"

    conversation_data = {"cats": {"contents": ['Welcome to the Channel'], "sent_by": ["Admin"], "sent_time": ["now"]},
           "dogs": {"contents": ['Welcome to the Channel'], "sent_by": ["Admin"], "sent_time": ["now"]}}

    if conversation_data.get(topic) == None:
        newTopic = {topic: {"contents": ['Welcome to the Channel'], "sent_by": ["Admin"], "sent_time": ["now"]}}
        conversation_data.update(newTopic)
        conversation_data[topic]["contents"].append(content)
        conversation_data[topic]["sent_by"].append(sent_by)
        conversation_data[topic]["sent_time"].append(sent_time)

        data = jsonify(conversation_data)
        return data


    else:
        conversation_data[topic]["contents"].append(content)
        conversation_data[topic]["sent_by"].append(sent_by)
        conversation_data[topic]["sent_time"].append(sent_time)

        data = jsonify(conversation_data)
        return data


@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    votes[selection] += 1
    emit("vote totals", votes, broadcast=True)



@app.route('/sign_out', methods=["POST"])
def sign_out():
    # remove the username from the session if it's there
    session.pop('user_name', None)
    return redirect(url_for('sign_in'))



if __name__ == "__main__":
    socketio.run(app)
