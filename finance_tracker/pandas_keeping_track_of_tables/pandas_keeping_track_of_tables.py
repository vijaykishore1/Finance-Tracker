import pandas as pd
from finance_tracker.constants.db_constants import SQLALCHEMY_DB_PATH
from sqlalchemy import create_engine
from finance_tracker.constants.table_names import LOGIN_TABLE, BANK_ACCOUNT_TABLE, INCOME_TABLE, INVESTMENTS_TABLE, \
    INVESTMENTS_CATEGORY_TABLE, INCOME_CATEGORY_TABLE, EXPENSES_TABLE, EXPENSES_CATEGORY_TABLE, USER_TABLE
import plotly.express as px

conn = create_engine(f"sqlite:///{SQLALCHEMY_DB_PATH}").connect()

df_login = pd.read_sql_table(LOGIN_TABLE, conn)
print(df_login.iloc[:, 0:4])
# print(df_login.columns)

df_bank_account = pd.read_sql_table(BANK_ACCOUNT_TABLE, conn)
print(df_bank_account.loc[df_bank_account['user_id'] == 2])
# fig = px.pie(df_bank_account.loc[df_bank_account['user_id'] == 2], values='amount', names='bank_name', title='Amount '
#                                                                                                              'in each'
#                                                                                                              ' bank')
# fig.show()

df_income = pd.read_sql_table(INCOME_TABLE, conn)
print(df_income)

df_investments = pd.read_sql_table(INVESTMENTS_TABLE, conn)
print(df_investments)

df_expenses = pd.read_sql_table(EXPENSES_TABLE, conn)
print(df_expenses.iloc[:, 0:5])

df_income_categories = pd.read_sql_table(INCOME_CATEGORY_TABLE, conn)
print(df_income_categories)

df_expenses_categories = pd.read_sql_table(EXPENSES_CATEGORY_TABLE, conn)
print(df_expenses_categories)

df_investments_categories = pd.read_sql_table(INVESTMENTS_CATEGORY_TABLE, conn)
print(df_investments_categories)

df_user = pd.read_sql_table(USER_TABLE, conn)
print(df_user)
