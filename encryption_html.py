from flask import Flask
import os
from cryptography.fernet import Fernet as Fer
# import pickle  # Will use later

# Intialize app
app = Flask(__name__, template_folder=os.getcwd())

@app.route("/")
def home():
    return "<b>Enter something to encrypt!</b>"

@app.route("/<raw>")
def encrypt(raw):
    key = Fer.generate_key()
    f = Fer(key)

    return f.decrypt(raw)
