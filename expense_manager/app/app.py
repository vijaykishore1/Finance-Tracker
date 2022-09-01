from flask import Flask, request
from expense_manager.controller.login_controller import LoginController
from expense_manager.controller.registration_controller import RegistrationController
from expense_manager.controller.bank_controller import BankController
from expense_manager.controller.income_controller import IncomeController
from expense_manager.controller.expenses_controller import ExpensesController
from expense_manager.controller.investments_controller import InvestmentsController
from expense_manager.constants.exception_constants import (
    USERNAME_DOES_NOT_EXIST_ERROR,
    BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR,
)
from expense_manager.db.db_utils import DbUtils

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
    response = RegistrationController().insert_registration_record(
        username=reg_data["username"],
        password=reg_data["password"],
        confirm_password=reg_data["confirm_password"],
        name=reg_data["name"],
        phone_number=reg_data["phone_number"],
    )
    return response


@app.route("/bankdetails", methods=["POST"])
def bank_details():
    bank_data = json.loads(request.data.decode("UTF-8"))
    print(bank_data["id"])
    if "amount" in bank_data:
        response = BankController.insert_bank_details(
            username=bank_data["username"],
            bank_name=bank_data["bank_name"],
            amount=bank_data["amount"],
        )
    else:
        response = BankController.insert_bank_details(
            username=bank_data["username"], bank_name=bank_data["bank_name"]
        )
    return response


# @app.route("/categories", methods=["POST"])
# def category():
#     category_data = json.loads(request.data.decode("UTF-8"))
#     assert "category" in category_data  # TODO
#     response = CategoriesController().insert_category_details(
#         category=category_data["category"], sub_category=category_data["sub_category"]
#     )
#     return response


@app.route("/income", methods=["POST"])
def income():
    income_data = json.loads(request.data.decode("UTF-8"))
    assert "bank_name" in income_data  # TODO
    response = IncomeController().insert_income_details(
        bank_name=income_data["bank_name"],
        username=income_data["username"],
        category=income_data["category"],
        sub_category=income_data["sub_category"],
        amount=income_data["amount"],
        date=income_data["date"],
        description=income_data["description"],
    )
    return response


@app.route("/expenses", methods=["POST"])
def expenses():
    expenses_data = json.loads(request.data.decode("UTF-8"))
    assert "bank_name" in expenses_data  # TODO
    response = ExpensesController().insert_expenses_details(
        bank_name=expenses_data["bank_name"],
        username=expenses_data["username"],
        category=expenses_data["category"],
        sub_category=expenses_data["sub_category"],
        amount=expenses_data["amount"],
        date=expenses_data["date"],
        description=expenses_data["description"],
    )
    return response


@app.route("/investments", methods=["POST"])
def investments():
    investments_data = json.loads(request.data.decode("UTF-8"))
    assert "bank_name" in investments_data  # TODO
    response = InvestmentsController().insert_investments_details(
        bank_name=investments_data["bank_name"],
        username=investments_data["username"],
        category=investments_data["category"],
        sub_category=investments_data["sub_category"],
        amount=investments_data["amount"],
        date=investments_data["date"],
        description=investments_data["description"],
    )
    return response


@app.route("/balance", methods=["GET"])
def balance():
    user_name = request.args.get("username")
    bankname = request.args.get("bank_name")
    # with DbUtils() as utils_obj:
    if not LoginController.is_username_exist(user_name):
        return USERNAME_DOES_NOT_EXIST_ERROR
    if not BankController.is_bank_account_exist(username=user_name, bank_name=bankname):
        return BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR
    curr_bal = BankController.get_balance(username=user_name, bank_name=bankname)
    return str(curr_bal)


if __name__ == "__main__":
    app.run(debug=True)
