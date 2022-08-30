from flask import Flask, request
from expense_manager.controller.login_controller import LoginController
from expense_manager.controller.registration_controller import RegistrationController
from expense_manager.controller.bank_controller import BankController
from expense_manager.controller.category_controller import CategoriesController
from expense_manager.controller.income_controller import IncomeController
from expense_manager.controller.expenses_controller import ExpensesController
from expense_manager.controller.investments_controller import InvestmentsController

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
@app.route("/bankdetails", methods=["POST"])
def bank_details():
    bank_data = json.loads(request.data.decode("UTF-8"))
    assert "bank_name" in bank_data #TODO
    response = BankController().bank_details(id=bank_data["id"],bank_name=bank_data["bank_name"],amount=bank_data["amount"])
    return response

@app.route("/categories", methods=["POST"])
def category():
    category_data = json.loads(request.data.decode("UTF-8"))
    assert "category" in category_data #TODO
    response = CategoriesController().category_details(category=category_data["category"],sub_category=category_data["sub_category"])
    return response

@app.route("/income", methods=["POST"])
def income():
    income_data = json.loads(request.data.decode("UTF-8"))
    assert "bank_name" in income_data #TODO
    response = IncomeController().income_details(bank_name=income_data["bank_name"],id=income_data["id"],source=income_data["source"],amount=income_data["amount"],date=income_data["date"],description=income_data["description"])
    return response

@app.route("/expenses", methods=["POST"])
def expenses():
    expenses_data = json.loads(request.data.decode("UTF-8"))
    assert "bank_name" in expenses_data #TODO
    response = ExpensesController().expenses_details(bank_name=expenses_data["bank_name"],id=expenses_data["id"],category_id=expenses_data["category_id"],amount=expenses_data["amount"],date=expenses_data["date"],description=expenses_data["description"])
    return response

@app.route("/investments", methods=["POST"])
def investments():
    investments_data = json.loads(request.data.decode("UTF-8"))
    assert "bank_name" in investments_data #TODO
    response = InvestmentsController().investments_details(bank_name=investments_data["bank_name"],id=investments_data["id"],type=investments_data["type"],amount=investments_data["amount"],date=investments_data["date"],description=investments_data["description"])
    return response

if __name__ == "__main__":
    app.run(debug=True)
