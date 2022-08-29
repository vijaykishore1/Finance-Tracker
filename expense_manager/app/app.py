from flask import Flask, request
from expense_manager.controller.login_controller import LoginController
import json

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    login_data = json.loads(request.data.decode("UTF-8"))
    assert "username" in login_data  # TODO
    response = LoginController().validate_login(
        username=login_data["username"], password=login_data["password"]
    )
    return response


# @app.route("/create", methods=["POST"]) #TODO
# def registration():


if __name__ == "__main__":
    app.run(debug=True)
