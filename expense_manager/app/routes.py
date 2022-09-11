from flask import request, render_template, url_for, flash, redirect
from expense_manager.app import app
from expense_manager.controller.registration_form import RegistrationForm, LoginForm
from expense_manager.controller.bank_controller import BankController
from expense_manager.controller.income_controller import IncomeController
from expense_manager.controller.expenses_controller import ExpensesController
from expense_manager.controller.investments_controller import InvestmentsController
from expense_manager.constants.exception_constants import (
    USERNAME_DOES_NOT_EXIST_ERROR,
    BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR,
)
from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.db_constants import DB_PATH
import json


