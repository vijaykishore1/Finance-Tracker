from expense_manager.db.db_schema_sql_alchemy import User, Login, BankAccount, Expenses, ExpensesCategories, \
    IncomeCategories, Income, InvestmentsCategories, Investments
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
user = Login.query.first()
print(user)


SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ExpenseManagerAlchemy.db'
db = SQLAlchemy(app)
user_1 = BankAccount(bank_name='HDFC', amount='10000', user_id=1)
db.session.add(user_1)
db.session.commit()
# print(User.query.all())
