from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


from expense_manager.constants.db_constants import SQLALCHEMY_DB_PATH

import os

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///" + SQLALCHEMY_DB_PATH
db = SQLAlchemy(app)

from expense_manager.app import routes
