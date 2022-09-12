import os
from finance_tracker.constants.constants import PROJECT_HOME

DB_PATH = os.path.join(PROJECT_HOME, "finance_tracker", "db", "ExpenseManager.db")
SQLALCHEMY_DB_PATH = os.path.join(PROJECT_HOME, "finance_tracker", "db", "ExpenseManagerAlchemy.db")

if __name__ == "__main__":
    print(SQLALCHEMY_DB_PATH)
