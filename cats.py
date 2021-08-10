from flask import Flask
from os import getcwd
# Get the location of the template
app = Flask(__name__, template_folder=getcwd())


@app.route("/<cats>")
def numOfCats(cats):
    try:
        if int(cats) == 0:
            return "You have no cats... how sad..."
        elif int(cats) == 1:
            return "You have 1 cat!"
        elif int(cats) < 5:
            return f"You have {cats} cats!"
        elif int(cats) > 5:
            return f"You have {cats} cats! That's alot!"
    except RuntimeError:
        print("Can not run for some reason")
