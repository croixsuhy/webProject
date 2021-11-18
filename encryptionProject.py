from flask import Flask, render_template, request
import os
from cryptography.fernet import Fernet as Fer

# Intialize app
app = Flask(__name__, template_folder=os.getcwd())


@app.route("/")
def home():
    # return "<b>Enter something to encrypt!</b>"

    return render_template("encryptionProject.html")


# Route back to the previous page to get the data
@app.route("/home", methods=["POST", "GET"])
def encrypt():

    try:
        # Flask will return this if there is nothing to work with
        if request.method == "POST":
            return "Make sure to enter something to encrypt!!"

        elif request.method == "GET":
            # Get data from HTML file
            raw = request.args.get("rawData")

            # Check to see if there is no data, else we pass it through
            if raw is None:
                return "There is no data!"

            else:
                # Encode, generate, and create a key
                raw = raw.encode()
                key = Fer.generate_key()
                f = Fer(key)

                encryptedString = f.encrypt(raw)
                decryptedString = f.decrypt(encryptedString)

                # Render template with variable in it
                return render_template("encryptionProjectDisplay.html", encrypted=str(encryptedString),
                                       decrypted=str(decryptedString))

    except RuntimeError:
        print("Cannot open HTML file, encrypt, or do anything")

    # # Temp
    # return str(f"""Encrypted string: {encryptedString}
    #             Decrypted string: {decryptedString}""")


# TEMP (DELETE/COMMENT AFTERWARDS!!!!!!!)
# if __name__ == "__main__":
#     app.debug = True
#     app.run()
