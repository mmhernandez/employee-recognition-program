from flask import Flask

app = Flask(__name__)
app.secret_key = "UEAjEsK9t4Z5EX3b1DrR"

# # Provide template folder name
# # The default folder name should be "templates" else need to mention custom folder name for template path
# # The default folder name for static files should be "static" else need to mention custom folder for static path
# app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')