import os
import secrets
from PIL import Image
from flask import request, render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from finance_tracker.app import app, db, bcrypt
from finance_tracker.controller.forms import RegistrationForm, LoginForm, UpdateAccountForm, BankDetailsForm, \
    IncomeForm, ExpensesForm, InvestmentsForm
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
@login_required
def home():
    banks = BankAccount.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', banks=banks)


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


@app.route("/incomedetails", methods=["GET", "POST"])
@login_required
def income_details():
    form = IncomeForm()
    if form.validate_on_submit():
        income_category_id_query = IncomeCategories.query.filter(
            IncomeCategories.income_category == form.income_category.data,
            IncomeCategories.income_sub_category == form.income_sub_category.data).first()
        if not income_category_id_query:
            incomecategory = IncomeCategories(income_category=form.income_category.data,
                                              income_sub_category=form.income_sub_category.data)
            db.session.add(incomecategory)
            db.session.commit()
            income_category_id_query = IncomeCategories.query.filter(
                IncomeCategories.income_category == form.income_category.data,
                IncomeCategories.income_sub_category == form.income_sub_category.data).first()

        existing_balance = BankAccount.query.filter(BankAccount.user_id == current_user.id,
                                                    BankAccount.bank_name == form.bank_name.data).first()
        income = Income(bank_name=form.bank_name.data, amount=form.amount.data,
                        user_id=current_user.id, income_category_id=income_category_id_query.income_category_id,
                        date=form.date.data, description=form.description.data)
        db.session.add(income)
        db.session.commit()
        income_bank_details = BankAccount.query.filter(BankAccount.user_id == current_user.id).first()
        income_bank_details.amount = existing_balance.amount + form.amount.data
        db.session.commit()

        flash('Your Income Details have been updated!', 'success')
        return redirect(url_for('home'))
    return render_template('income_details.html', title='Income Details', form=form)


@app.route("/expensesdetails", methods=["GET", "POST"])
@login_required
def expenses_details():
    form = ExpensesForm()
    if form.validate_on_submit():
        expenses_category_id_query = ExpensesCategories.query.filter(
            ExpensesCategories.expenses_category == form.expenses_category.data,
            ExpensesCategories.expenses_sub_category == form.expenses_sub_category.data).first()
        if not expenses_category_id_query:
            expensescategory = ExpensesCategories(expenses_category=form.expenses_category.data,
                                                  expenses_sub_category=form.expenses_sub_category.data)
            db.session.add(expensescategory)
            db.session.commit()
            expenses_category_id_query = ExpensesCategories.query.filter(
                ExpensesCategories.expenses_category == form.expenses_category.data,
                ExpensesCategories.expenses_sub_category == form.expenses_sub_category.data).first()

        existing_balance = BankAccount.query.filter(BankAccount.user_id == current_user.id,
                                                    BankAccount.bank_name == form.bank_name.data).first()
        expenses = Expenses(bank_name=form.bank_name.data, amount=form.amount.data,
                            user_id=current_user.id,
                            expenses_category_id=expenses_category_id_query.expenses_category_id,
                            date=form.date.data, description=form.description.data)
        db.session.add(expenses)
        db.session.commit()
        expenses_bank_details = BankAccount.query.filter(BankAccount.user_id == current_user.id).first()
        expenses_bank_details.amount = existing_balance.amount - form.amount.data
        db.session.commit()

        flash('Your Expense Details have been updated!', 'success')
        return redirect(url_for('home'))
    return render_template('expenses_details.html', title='Expense Details', form=form)


@app.route("/investmentsdetails", methods=["GET", "POST"])
@login_required
def investments_details():
    form = InvestmentsForm()
    if form.validate_on_submit():
        investments_category_id_query = InvestmentsCategories.query.filter(
            InvestmentsCategories.investments_category == form.investments_category.data,
            InvestmentsCategories.investments_sub_category == form.investments_sub_category.data).first()
        if not investments_category_id_query:
            investmentscategory = InvestmentsCategories(investments_category=form.investments_category.data,
                                                        investments_sub_category=form.investments_sub_category.data)
            db.session.add(investmentscategory)
            db.session.commit()
            investments_category_id_query = InvestmentsCategories.query.filter(
                InvestmentsCategories.investments_category == form.investments_category.data,
                InvestmentsCategories.investments_sub_category == form.investments_sub_category.data).first()

        existing_balance = BankAccount.query.filter(BankAccount.user_id == current_user.id,
                                                    BankAccount.bank_name == form.bank_name.data).first()
        investments = Investments(bank_name=form.bank_name.data, amount=form.amount.data,
                                  user_id=current_user.id,
                                  investments_category_id=investments_category_id_query.investments_category_id,
                                  date=form.date.data, description=form.description.data)
        db.session.add(investments)
        db.session.commit()
        investments_bank_details = BankAccount.query.filter(BankAccount.user_id == current_user.id).first()
        investments_bank_details.amount = existing_balance.amount - form.amount.data
        db.session.commit()

        flash('Your Investment Details have been updated!', 'success')
        return redirect(url_for('home'))
    return render_template('investments_details.html', title='Investment Details', form=form)


##########################HAVE COMMENTED EVERYTHING BELOW FOR THE TIME BEING#########################################


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
#     return render_template('bank_details.html', title='Bank Accounts', body=ans)
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
