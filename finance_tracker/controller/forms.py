from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from finance_tracker.db.models import User, Login, BankAccount, Income, IncomeCategories


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    @staticmethod
    def validate_username(self, username):
        user = Login.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken. Please choose a new one')

    @staticmethod
    def validate_email(self, email):
        user = Login.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That Email is taken. Please choose a new one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    @staticmethod
    def validate_username(self, username):
        if username.data != current_user.username:
            user = Login.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is taken. Please choose a new one')

    @staticmethod
    def validate_email(self, email):
        if email.data != current_user.email:
            user = Login.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That Email is taken. Please choose a new one')


class BankDetailsForm(FlaskForm):
    bank_name = StringField('Bank Name', validators=[DataRequired(), Length(min=2, max=20)])
    amount = IntegerField('Bank Balance')
    submit = SubmitField('Update Bank Details')

    @staticmethod
    def validate_bank_name(self, bank_name):
        bank_exist = BankAccount.query.filter(BankAccount.bank_name == bank_name.data,
                                              Login.id == current_user.id).all()
        if bank_exist:
            raise ValidationError("You already have an account in this bank")


class IncomeForm(FlaskForm):
    # bank_name, user_id, income_category, income_sub_category, amount, date, description
    bank_name = StringField('Bank Name', validators=[DataRequired(), Length(min=2, max=20)])
    amount = IntegerField('Amount', validators=[DataRequired()])
    income_category = StringField('Category', validators=[DataRequired(), Length(min=2, max=20)])
    income_sub_category = StringField('Sub Category', validators=[DataRequired(), Length(min=2, max=20)])
    date = DateField('Date of income', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    submit = SubmitField('Update Income Details')

    @staticmethod
    def validate_bank_name(self, bank_name):
        bank_exist = BankAccount.query.filter(BankAccount.bank_name == bank_name.data,
                                              Login.id == current_user.id).all()
        if not bank_exist:
            raise ValidationError("You don't have an account in this bank")


class ExpensesForm(FlaskForm):
    # bank_name, user_id, expenses_category, expenses_sub_category, amount, date, description
    bank_name = StringField('Bank Name', validators=[DataRequired(), Length(min=2, max=20)])
    amount = IntegerField('Amount', validators=[DataRequired()])
    expenses_category = StringField('Category', validators=[DataRequired(), Length(min=2, max=20)])
    expenses_sub_category = StringField('Sub Category', validators=[DataRequired(), Length(min=2, max=20)])
    date = DateField('Date of expense', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    submit = SubmitField('Update Expense Details')

    @staticmethod
    def validate_bank_name(self, bank_name):
        bank_exist = BankAccount.query.filter(BankAccount.bank_name == bank_name.data,
                                              Login.id == current_user.id).all()
        if not bank_exist:
            raise ValidationError("You don't have an account in this bank")


class InvestmentsForm(FlaskForm):
    # bank_name, user_id, investments_category, investments_sub_category, amount, date, description
    bank_name = StringField('Bank Name', validators=[DataRequired(), Length(min=2, max=20)])
    amount = IntegerField('Amount', validators=[DataRequired()])
    investments_category = StringField('Category', validators=[DataRequired(), Length(min=2, max=20)])
    investments_sub_category = StringField('Sub Category', validators=[DataRequired(), Length(min=2, max=20)])
    date = DateField('Date of investments', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    submit = SubmitField('Update Investment Details')

    @staticmethod
    def validate_bank_name(self, bank_name):
        bank_exist = BankAccount.query.filter(BankAccount.bank_name == bank_name.data,
                                              Login.id == current_user.id).all()
        if not bank_exist:
            raise ValidationError("You don't have an account in this bank")
