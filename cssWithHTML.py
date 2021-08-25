from flask import Flask
from flask import render_template
from os import getcwd

app = Flask(__name__, template_folder=getcwd())


@app.route("/")
def home():
    return render_template("cssTest.html")


# Temp
app.run()
