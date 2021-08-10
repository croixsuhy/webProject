from flask import Flask
from os import getcwd
# Get the location of the template
app = Flask(__name__, template_folder=getcwd())

# Main page
@app.route("/")
def home():
    return "<title>Enter how many cats you own in the search bar!</title>"

# /<cats> makes it so you can use an input in the search bar
@app.route("/<cats>")
def numOfCats(cats):
    try:
        try:
            # Changes cats variable to an int
            if int(cats) == 0:
                return "You have no cats... how sad..."
            elif int(cats) == 1:
                return "You have a cat! Go get some more!"
            elif int(cats) < 5:
                return f"You have {cats} cats!"
            elif int(cats) > 5:
                return f"You have {cats} cats! That's alot!"

        except:
            return "Can not run (our cats are having issues running the site...)"

    except RuntimeError:
        print("Application can not run")
