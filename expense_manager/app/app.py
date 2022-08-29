from flask import Flask, request
from expense_manager.controller.login_controller import LoginController
from expense_manager.controller.registration_controller import RegistrationController
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

@app.route("/registrationform", methods=["POST"])
def registration_form():
    reg_data = json.loads(request.data.decode("UTF-8"))
    assert "username" in reg_data  # TODO
    response = RegistrationController().registration(username=reg_data["username"], password=reg_data["password"],confirm_password=reg_data["confirm_password"],name=reg_data["name"],phone_number=reg_data["phone_number"])
    return response
# @app.route("/create", methods=["POST"]) #TODO
# def registration():


if __name__ == "__main__":
    app.run(debug=True)
