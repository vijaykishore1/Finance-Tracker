from flask import render_template

USERNAME_DOES_NOT_EXIST_ERROR = "username does not exist"
PASSWORD_NOT_VALIDATED = "Password is incorrect. Please try again"
USERNAME_ALREADY_EXISTS_ERROR = "username already exists. please try a new one"
PASSWORDS_DONT_MATCH_ERROR = "Passwords do not match, enter again"
BANK_ACCOUNT_ALREADY_EXISTS_ERROR = "You already have an account in this bank."
CATEGORY_ALREADY_EXISTS_ERROR = "This category already exists"
SUB_CATEGORY_ALREADY_EXISTS_ERROR = "This sub category already exists"
INCOME_RECORD_ALREADY_EXISTS_ERROR = "This income record already exists."
BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR = "You don't have an account in this bank"
EXPENSES_RECORD_ALREADY_EXISTS_ERROR = "This expense record already exists."
INSUFFICIENT_BALANCE = "There is not enough balance in your account to make this expense"
INVESTMENTS_RECORD_ALREADY_EXISTS_ERROR = "This investment record already exists."
USERNAME_CANNOT_BE_NULL = "Username cannot be null. Please enter a username"
NOT_NULL_CONSTRAINT = "Cannot be NULL. Please enter valid value"
