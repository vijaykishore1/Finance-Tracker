from datetime import datetime
from expense_manager.app import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from expense_manager.constants.db_constants import SQLALCHEMY_DB_PATH
import os


class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Login('{self.username}','{self.email}', '{self.image_file}')"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.String(15))
    user_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.phone_number}')"


class BankAccount(db.Model):
    bank_id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)

    def __repr__(self):
        return f"BankAccount('{self.bank_name}', '{self.amount}')"


class ExpensesCategories(db.Model):
    __tablename__ = 'expensescategories'
    expenses_category_id = db.Column(db.Integer, primary_key=True)
    expenses_category = db.Column(db.String(40), nullable=False)
    expenses_sub_category = db.Column(db.String(40), default=None)

    def __repr__(self):
        return f"User('{self.expenses_category}', '{self.expenses_sub_category}')"


class InvestmentsCategories(db.Model):
    __tablename__ = 'investmentscategories'
    investments_category_id = db.Column(db.Integer, primary_key=True)
    investments_category = db.Column(db.String(40), nullable=False)
    investments_sub_category = db.Column(db.String(40), default=None)

    def __repr__(self):
        return f"User('{self.investments_category}', '{self.investments_sub_category}')"


class IncomeCategories(db.Model):
    __tablename__ = 'incomecategories'
    income_category_id = db.Column(db.Integer, primary_key=True)
    income_category = db.Column(db.String(40), nullable=False)
    income_sub_category = db.Column(db.String(40), default=None)

    def __repr__(self):
        return f"User('{self.income_category}', '{self.income_sub_category}')"


class Expenses(db.Model):

    expenses_id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)
    expenses_category_id = db.Column(db.String(40), db.ForeignKey('expensescategories.expenses_category_id'),
                                     nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User('{self.bank_name}', '{self.amount}', '{self.description}', '{self.date}')"


class Investments(db.Model):
    investments_id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)
    investments_category_id = db.Column(db.String(40), db.ForeignKey('investmentscategories.investments_category_id'),
                                        nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User('{self.bank_name}', '{self.amount}', '{self.description}', '{self.date}')"


class Income(db.Model):
    income_id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)
    income_category_id = db.Column(db.String(40), db.ForeignKey('incomecategories.income_category_id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User('{self.bank_name}', '{self.amount}', '{self.description}', '{self.date}')"

# db.create_all()


if __name__ == '__main__':

    # user_1 = User(name = 'Vijay Kishore', phone_number = '9876543210')
    # db.session.add(user_1)
    # db.session.commit()
    print(Login.query.all())
