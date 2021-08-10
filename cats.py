from flask import Flask
from os import getcwd
# Get the location of the template
app = Flask(__name__, template_folder=getcwd())


# /<cats> makes it so you can use an input in the search bar
@app.route("/<cats>")
def numOfCats(cats):
    try:
        if int(cats) == None:
            return "<title>Enter a number in the search bar!</title>"
        # Changes cats variable to an int
        elif int(cats) == 0:
            return "You have no cats... how sad..."
        elif int(cats) == 1:
            return "You have a cat! Go get some more!"
        elif int(cats) < 5:
            return f"You have {cats} cats!"
        elif int(cats) > 5:
            return f"You have {cats} cats! That's alot!"
    except RuntimeError:
        print("Can not run")
