import os
import secrets
from PIL import Image
from flask import request, render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from finance_tracker.app import app, db, bcrypt
from finance_tracker.controller.forms import RegistrationForm, LoginForm, UpdateAccountForm, BankDetailsForm
from finance_tracker.controller.bank_controller import BankController
from finance_tracker.controller.income_controller import IncomeController
from finance_tracker.controller.expenses_controller import ExpensesController
from finance_tracker.controller.investments_controller import InvestmentsController
from finance_tracker.controller.get_user_details import GetDetails
from finance_tracker.db.models import User, Login, BankAccount, ExpensesCategories, \
    InvestmentsCategories, IncomeCategories, Expenses, Income, Investments

import json


@app.route("/")
@app.route("/home")
def home():
    bank = BankAccount.query.all()
    return render_template('home.html', bank=bank)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Login.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_filename)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_filename


@app.route("/account", methods=["POST", "GET"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename=f'profile_pics/{current_user.image_file}')

    return render_template('account.html', title='Account', image_file=image_file, form=form)


##########################HAVE COMMENTED EVERYTHING BELOW FOR THE TIME BEING#########################################

@app.route("/bankdetails", methods=["GET", "POST"])
@login_required
def bank_details():
    form = BankDetailsForm()
    if form.validate_on_submit():
        bank = BankAccount(bank_name=form.bank_name.data, amount=form.amount.data, user_id=current_user.id)
        db.session.add(bank)
        db.session.commit()
        flash('Your Bank Details have been updated!', 'success')
        return redirect(url_for('home'))
    return render_template('bank_details.html', title='Bank Details', form=form)


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
    if "sub_category" in income_data:
        response = IncomeController().insert_income_details(
            bank_name=income_data["bank_name"],
            username=income_data["username"],
            category=income_data["category"],
            sub_category=income_data["sub_category"],
            amount=income_data["amount"],
            date=income_data["date"],
            description=income_data["description"],
        )
    else:
        response = IncomeController().insert_income_details(
            bank_name=income_data["bank_name"],
            username=income_data["username"],
            category=income_data["category"],
            amount=income_data["amount"],
            date=income_data["date"],
            description=income_data["description"],
        )
    return response


@app.route("/expenses", methods=["POST"])
def expenses():
    # sourcery skip: assign-if-exp, inline-immediately-returned-variable
    expenses_data = json.loads(request.data.decode("UTF-8"))
    assert "bank_name" in expenses_data  # TODO
    if "sub_category" in expenses_data:
        response = ExpensesController().insert_expenses_details(
            bank_name=expenses_data["bank_name"],
            username=expenses_data["username"],
            category=expenses_data["category"],
            sub_category=expenses_data["sub_category"],
            amount=expenses_data["amount"],
            date=expenses_data["date"],
            description=expenses_data["description"],
        )
    else:
        response = ExpensesController().insert_expenses_details(
            bank_name=expenses_data["bank_name"],
            username=expenses_data["username"],
            category=expenses_data["category"],
            amount=expenses_data["amount"],
            date=expenses_data["date"],
            description=expenses_data["description"],
        )
    return response


@app.route("/investments", methods=["POST"])
def investments():
    # sourcery skip: assign-if-exp, inline-immediately-returned-variable
    investments_data = json.loads(request.data.decode("UTF-8"))
    assert "bank_name" in investments_data  # TODO
    if "sub_category" in investments_data:
        response = InvestmentsController().insert_investments_details(
            bank_name=investments_data["bank_name"],
            username=investments_data["username"],
            category=investments_data["category"],
            sub_category=investments_data["sub_category"],
            amount=investments_data["amount"],
            date=investments_data["date"],
            description=investments_data["description"],
        )
    else:
        response = InvestmentsController().insert_investments_details(
            bank_name=investments_data["bank_name"],
            username=investments_data["username"],
            category=investments_data["category"],
            amount=investments_data["amount"],
            date=investments_data["date"],
            description=investments_data["description"],
        )
    return response


@app.route("/getdetails/balance", methods=["GET"])
def balance():
    user_name = request.args.get("username")
    ans = GetDetails.get_balance_of_user(username=user_name)
    return render_template('balance.html', title='Balance', body=ans)


@app.route("/getdetails/logindetails", methods=["GET"])
def logindetails():
    user_name = request.args.get("username")
    ans = GetDetails.get_login_details_of_user(username=user_name)
    return render_template('logindetails.html', title='Login Details', body=ans)


@app.route("/getdetails/user_bio", methods=["GET"])
def user_bio():
    user_name = request.args.get("username")
    ans = GetDetails.get_bio_of_user(username=user_name)
    return render_template('user_bio.html', title='User Details', body=ans)


@app.route("/getdetails/bank_accounts", methods=["GET"])
def bank_accounts():
    user_name = request.args.get("username")
    ans = GetDetails.get_bank_accounts_of_user(username=user_name)
    return render_template('bank_details.html', title='Bank Accounts', body=ans)


@app.route("/getdetails/income_details", methods=["GET"])
def income_details():
    user_name = request.args.get("username")
    ans = GetDetails.get_income_details_of_user(username=user_name)
    return render_template('income_details.html', title='Income Details', body=ans)


@app.route("/getdetails/expenses_details", methods=["GET"])
def expenses_details():
    user_name = request.args.get("username")
    ans = GetDetails.get_expenses_details_of_user(username=user_name)
    return render_template('expenses_details.html', title='Expenses Details', body=ans)


@app.route("/getdetails/investments_details", methods=["GET"])
def investments_details():
    user_name = request.args.get("username")
    ans = GetDetails.get_investments_details_of_user(username=user_name)
    return render_template('investments_details.html', title='Investments Details', body=ans)


@app.route("/getdetails/all", methods=["GET"])
def all_details():
    user_name = request.args.get("username")
    ans = GetDetails.get_all_details_of_user(username=user_name)
    return render_template('all_details.html', title='All Details', body=ans)
