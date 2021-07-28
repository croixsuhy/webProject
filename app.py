from flask import Flask, render_template
from os import getcwd
# Get the location of the template
app = Flask(__name__, template_folder=getcwd())


@app.route("/")
def home():
    # Use the html file
    return render_template("test.html")


app.run(port=8080)
