from flask import Flask, render_template, request, flash, session, redirect, url_for, g
# from flask_session import Session
from flask_socketio import SocketIO

app = Flask(__name__, template_folder="templates")
app.secret_key = "hfow875^&i3%3425tv9;2^$"

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
socketio = SocketIO(app)