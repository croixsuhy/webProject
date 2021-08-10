from flask import Flask
from flask import render_template
from os import getcwd

# Initalize app
app = Flask(__name__, template_folder=getcwd())

@app.route("/")
def list():
    # List of fruits
    fruits = list(range(10))

    # Render template and use list
    return render_template("listTest.html", title="Fruits", fruits=fruits)
