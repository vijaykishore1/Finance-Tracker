from flask import Flask, request
from expense_manager.controller.login_controller import LoginController
import json

app = Flask(__name__)


@app.route("/login")
def login():
    response = LoginController().validate_login(username="", password="")
    return response

