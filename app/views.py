__author__ = 'claytonpeterson'

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


def main_view():
    """
    configures the window to show the main view
    """
    pass


def client_view():
    """
    configures the window to show the client view
    """


def server_view():
    """
    configures the window to show the server view
    """


def client_view():
    """
    configures the window to show the config view
    """


def say_hi():
    print "hi!"
