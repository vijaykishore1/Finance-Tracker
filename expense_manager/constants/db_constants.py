import os
from expense_manager.constants.constants import PROJECT_HOME

DB_PATH = os.path.join(PROJECT_HOME, "expense_manager", "db", "ExpenseManager.db")
SQLALCHEMY_DB_PATH = "sqlite3:////expense_manager/db/ExpenseManagerAlchemy.db"

if __name__ == "__main__":
    print(DB_PATH)
