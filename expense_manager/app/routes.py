from flask import request, render_template, url_for, flash, redirect
from expense_manager.app import app
from expense_manager.controller.forms import RegistrationForm, LoginForm
# from expense_manager.controller.bank_controller import BankController
# from expense_manager.controller.income_controller import IncomeController
# from expense_manager.controller.expenses_controller import ExpensesController
# from expense_manager.controller.investments_controller import InvestmentsController

from expense_manager.db.db_schema_sql_alchemy import User, Login, BankAccount, ExpensesCategories, \
    InvestmentsCategories, IncomeCategories, Expenses, Income, Investments

import json


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


# @app.route("/login", methods=["POST"])
# def login():
#     login_data = json.loads(request.data.decode("UTF-8"))
#     assert "username" in login_data  # TODO
#     response = LoginController().validate_login(
#         username=login_data["username"], password=login_data["password"]
#     )
#     return response
#
#
# @app.route("/registrationform", methods=["POST"])
# def registration_form():
#     reg_data = json.loads(request.data.decode("UTF-8"))
#     assert "username" in reg_data  # TODO
#     response = RegistrationController().insert_registration_record(
#         username=reg_data["username"],
#         password=reg_data["password"],
#         confirm_password=reg_data["confirm_password"],
#         name=reg_data["name"],
#         phone_number=reg_data["phone_number"],
#     )
#     return response

@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Login(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created, you are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('Register.html', title='Register', form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "admin123":
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('Login.html', title='Login', form=form)


##########################HAVE COMMENTED EVERYTHING BELOW FOR THE TIME BEING#########################################

# @app.route("/bankdetails", methods=["POST"])
# def bank_details():
#     bank_data = json.loads(request.data.decode("UTF-8"))
#     print(bank_data["id"])
#     if "amount" in bank_data:
#         response = BankController.insert_bank_details(
#             username=bank_data["username"],
#             bank_name=bank_data["bank_name"],
#             amount=bank_data["amount"],
#         )
#     else:
#         response = BankController.insert_bank_details(
#             username=bank_data["username"], bank_name=bank_data["bank_name"]
#         )
#     return response
#
#
# # @app.route("/categories", methods=["POST"])
# # def category():
# #     category_data = json.loads(request.data.decode("UTF-8"))
# #     assert "category" in category_data  # TODO
# #     response = CategoriesController().insert_category_details(
# #         category=category_data["category"], sub_category=category_data["sub_category"]
# #     )
# #     return response
#
#
# @app.route("/income", methods=["POST"])
# def income():
#     income_data = json.loads(request.data.decode("UTF-8"))
#     assert "bank_name" in income_data  # TODO
#     if "sub_category" in income_data:
#         response = IncomeController().insert_income_details(
#             bank_name=income_data["bank_name"],
#             username=income_data["username"],
#             category=income_data["category"],
#             sub_category=income_data["sub_category"],
#             amount=income_data["amount"],
#             date=income_data["date"],
#             description=income_data["description"],
#         )
#     else:
#         response = IncomeController().insert_income_details(
#             bank_name=income_data["bank_name"],
#             username=income_data["username"],
#             category=income_data["category"],
#             amount=income_data["amount"],
#             date=income_data["date"],
#             description=income_data["description"],
#         )
#     return response
#
#
# @app.route("/expenses", methods=["POST"])
# def expenses():
#     expenses_data = json.loads(request.data.decode("UTF-8"))
#     assert "bank_name" in expenses_data  # TODO
#     if "sub_category" in expenses_data:
#         response = ExpensesController().insert_expenses_details(
#             bank_name=expenses_data["bank_name"],
#             username=expenses_data["username"],
#             category=expenses_data["category"],
#             sub_category=expenses_data["sub_category"],
#             amount=expenses_data["amount"],
#             date=expenses_data["date"],
#             description=expenses_data["description"],
#         )
#     else:
#         response = ExpensesController().insert_expenses_details(
#             bank_name=expenses_data["bank_name"],
#             username=expenses_data["username"],
#             category=expenses_data["category"],
#             amount=expenses_data["amount"],
#             date=expenses_data["date"],
#             description=expenses_data["description"],
#         )
#     return response
#
#
# @app.route("/investments", methods=["POST"])
# def investments():
#     investments_data = json.loads(request.data.decode("UTF-8"))
#     assert "bank_name" in investments_data  # TODO
#     if "sub_category" in investments_data:
#         response = InvestmentsController().insert_investments_details(
#             bank_name=investments_data["bank_name"],
#             username=investments_data["username"],
#             category=investments_data["category"],
#             sub_category=investments_data["sub_category"],
#             amount=investments_data["amount"],
#             date=investments_data["date"],
#             description=investments_data["description"],
#         )
#     else:
#         response = InvestmentsController().insert_investments_details(
#             bank_name=investments_data["bank_name"],
#             username=investments_data["username"],
#             category=investments_data["category"],
#             amount=investments_data["amount"],
#             date=investments_data["date"],
#             description=investments_data["description"],
#         )
#     return response
#
#
# @app.route("/getdetails/balance", methods=["GET"])
# def balance():
#     user_name = request.args.get("username")
#     ans = GetDetails.get_balance_of_user(username=user_name)
#     return render_template('balance.html', title='Balance', body=ans)
#
#
# @app.route("/getdetails/logindetails", methods=["GET"])
# def logindetails():
#     user_name = request.args.get("username")
#     ans = GetDetails.get_login_details_of_user(username=user_name)
#     return render_template('logindetails.html', title='Login Details', body=ans)
#
#
# @app.route("/getdetails/user_bio", methods=["GET"])
# def user_bio():
#     user_name = request.args.get("username")
#     ans = GetDetails.get_bio_of_user(username=user_name)
#     return render_template('user_bio.html', title='User Details', body=ans)
#
#
# @app.route("/getdetails/bank_accounts", methods=["GET"])
# def bank_accounts():
#     user_name = request.args.get("username")
#     ans = GetDetails.get_bank_accounts_of_user(username=user_name)
#     return render_template('bank_accounts.html', title='Bank Accounts', body=ans)
#
#
# @app.route("/getdetails/income_details", methods=["GET"])
# def income_details():
#     user_name = request.args.get("username")
#     ans = GetDetails.get_income_details_of_user(username=user_name)
#     return render_template('income_details.html', title='Income Details', body=ans)
#
#
# @app.route("/getdetails/expenses_details", methods=["GET"])
# def expenses_details():
#     user_name = request.args.get("username")
#     ans = GetDetails.get_expenses_details_of_user(username=user_name)
#     return render_template('expenses_details.html', title='Expenses Details', body=ans)
#
#
# @app.route("/getdetails/investments_details", methods=["GET"])
# def investments_details():
#     user_name = request.args.get("username")
#     ans = GetDetails.get_investments_details_of_user(username=user_name)
#     return render_template('investments_details.html', title='Investments Details', body=ans)
#
#
# @app.route("/getdetails/all", methods=["GET"])
# def all_details():
#     user_name = request.args.get("username")
#     ans = GetDetails.get_all_details_of_user(username=user_name)
#     return render_template('all_details.html', title='All Details', body=ans)
