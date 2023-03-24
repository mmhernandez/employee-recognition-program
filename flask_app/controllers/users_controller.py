from flask_app import app
from flask import render_template


@app.route("/")
def home():
    return render_template("home.html")





# BADGES
@app.route("/badges")
def badges():
    # need to add session check to protect route
    return render_template("badges.html")