from flask import Flask, render_template, request, redirect, url_for, abort
import os
from cryptography.fernet import Fernet as Fer

# Intialize app
app = Flask(__name__, template_folder=os.getcwd())


@app.route("/")
def homepage():
    return render_template("homepage.html")


"""----------------- Text Encrypting -------------------"""

@app.route("/textEncrypt")
def textEncrypt():
    # return "<b>Enter something to encrypt!</b>"

    return render_template("textEncryption.html")


# Route back to the previous page to get the data
@app.route("/home", methods=["GET", "POST"])
def textEncrypting():
    try:
        if request.method == "POST":
            # Get data from HTML file
            raw = request.args.get("rawData")

            # Safety net if the program gets nothing (meaning None, not an empty string)
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
                # THE HTML IS TEMPORARY we will put it on the same page
                return render_template("textEncryptionDisplayTEMP.html", encrypted=str(encryptedString),
                                       decrypted=str(decryptedString), key=str(key))

    except RuntimeError:
        # Return a 404 Not Found error
        abort(404)


"""--------------------------------------------------"""

"""----------------- File Encrypting ----------------"""


@app.route("/fileEncrypt")
def fileEncrypt():
    return render_template("fileEncryption.html")


@app.route("/fileEncrypt", methods=["POST"])
def fileEncryption():
    if request.method == "POST":
        try:
            rawFile = request.files["rawFile"]

            if rawFile.filename == "":
                return "There is no data!"

        except RuntimeError:
            # Return a 404 Not Found error
            abort(404)


# TEMP (DELETE/COMMENT AFTERWARDS!!!!!!!)
if __name__ == "__main__":
    app.run(debug=True)
