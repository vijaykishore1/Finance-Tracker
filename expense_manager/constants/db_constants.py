import os
from expense_manager.constants.constants import PROJECT_HOME

DB_PATH = os.path.join(PROJECT_HOME, "expense_manager", "db", "ExpenseManager.db")
SQLALCHEMY_DB_PATH = os.path.join(PROJECT_HOME, "expense_manager", "db", "ExpenseManagerAlchemy.db")
# for i in SQLALCHEMY_DB_PATH:
#     if i == "\\":
#         i = "/"

if __name__ == "__main__":
    print(SQLALCHEMY_DB_PATH)
