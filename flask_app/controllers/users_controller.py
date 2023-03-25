from flask_app import app
from flask import render_template


@app.route("/")
def home():
    return render_template("home.html")


### ADMIN AND/OR HR USER ###
# BADGES
@app.route("/badge/new")
def new_badge():
    # need to add session check to protect route
    return render_template("admin_new_badge.html")

### STAFF USER ###
# BADGES
@app.route("/badges")
def badges():
    # need to add session check to protect route
    return render_template("badges.html")