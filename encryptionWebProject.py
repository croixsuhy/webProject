from flask import Flask
from flask import render_template
import firebase_admin
from firebase_admin import credentials
from os import getcwd

app = Flask(__name__, template_folder=getcwd())

# Service credentials for Firebase
cred = credentials.Certificate("web-encryption-project-firebase-adminsdk-2ta1a4-9ea67fe74f.json")

# Initalize app
firebase_admin.initialize_app(cred)

@app.route("/")
def home():
    pass
