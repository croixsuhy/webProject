from flask import Flask, render_template, request, redirect, url_for, abort, send_file
import os
from cryptography.fernet import Fernet as Fer
from werkzeug.utils import secure_filename

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
        if request.method == "GET":
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
            # Request for file to encrypt
            # .read() allows us to get the bytes-content out of the file
            rawFile = request.files["rawFile"].read()

            # Split text characters
            rawTxt = rawFile.split(b"\r\n")

            # Create a random key that will be used
            encTxt = []
            randomKey = Fer.generate_key()
            f = Fer(randomKey)

            # Encrypt items in list and append to the encrypted text list
            for rawLine in rawTxt:
                encTxt.append(f.encrypt(rawLine))

            # Create/open a text file and dump encrypted content and key into file
            if not os.path.exists(".\\encryptedText.txt"):
                with open("encryptedText.txt", "x") as encryptedFile:
                    encryptedFile.write(f"Key: {randomKey}\n\r")
                    encryptedFile.write("Data:\n\r~")
                    for encLine in encTxt:
                        encryptedFile.write(f"{encLine}\r")

            else:
                with open("encryptedText.txt", "w") as encryptedFile:
                    encryptedFile.write(f"Key: {randomKey.decode()}\n\r")
                    encryptedFile.write("Data:\n\r")
                    for encLine in encTxt:
                        encryptedFile.write(f"{encLine.decode()}\r")

            # Send the file and make the user download it
            return send_file(".\\encryptedText.txt", download_name="encryptedText.txt", as_attachment=True)

        except RuntimeError:
            # Return a 404 Not Found error
            abort(404)


# TEMP (DELETE/COMMENT AFTERWARDS!!!!!!!)
if __name__ == "__main__":
    app.run(debug=True)
