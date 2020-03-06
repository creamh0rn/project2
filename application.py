import os

from flask import Flask, render_template, session, redirect, url_for
from flask_socketio import SocketIO, emit
from flask_session import Session


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/", methods=["GET"])
def index():
    if session.get("user_name") == None:
        return redirect(url_for("sign_in"))
    else:


        return render_template("index.html", cum_dump = "running")

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    return render_template("sign_in.html")



if __name__ == "__main__":
    socketio.run(app)