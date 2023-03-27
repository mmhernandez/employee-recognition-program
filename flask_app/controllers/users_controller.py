from flask_app import app
from flask import render_template, redirect, request, session
import os

# CLOUDINARAY
from dotenv import load_dotenv
load_dotenv()
import cloudinary
import cloudinary.uploader
import cloudinary.api


config = cloudinary.config(secure = True)


@app.route("/")
def home():
    return render_template("home.html")


### ADMIN AND/OR HR USER ###
# BADGES
@app.route("/badge/new")
def new_badge():
    # need to add session check to protect route
    return render_template("admin_new_badge.html")

@app.route("/create_badge", methods=["POST"])
def insert_badge():
    print(f'request.form = {request.form}')

    uploaded_img = request.files['image']

    folder = "badges"

    # Upload the image: set the asset's public ID and allow overwriting the asset with new versions
    cloudinary.uploader.upload(uploaded_img, folder=folder, public_id=request.form["name"], unique_filename=False, overwrite=True, tags=request.form["category"])

    # Build the URL for the image and save it in the variable 'srcURL'
    srcURL = cloudinary.CloudinaryImage(f'badges/{request.form["name"]}').build_url()

    # Log the image URL to the console.
    # Copy this URL in a browser tab to generate the image on the fly.
    print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")

    return redirect ("/badges")

### STAFF USER ###
# BADGES
@app.route("/badges")
def badges():
    # need to add session check to protect route
    return render_template("badges.html")