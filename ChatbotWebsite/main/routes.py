from flask import render_template
from flask import Blueprint
from flask_login import current_user, login_required

main = Blueprint("main", __name__)


# Home Page
@main.route("/")
def home():
    return render_template("home.html", title="Mental Health Chatbot")


# About Page
@main.route("/about")
def about():
    return render_template("about.html", title="About")


# SOS Page
@main.route("/sos")
def sos():
    return render_template("sos.html", title="SOS")
