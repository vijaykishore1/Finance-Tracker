import pandas as pd
from finance_tracker.db.db_utils import DbUtils
from finance_tracker.constants.table_names import LOGIN_TABLE, EXPENSES_TABLE, EXPENSES_CATEGORY_TABLE, \
    INCOME_CATEGORY_TABLE, INVESTMENTS_CATEGORY_TABLE, INVESTMENTS_TABLE, INCOME_TABLE, BANK_ACCOUNT_TABLE, USER_TABLE

with DbUtils() as utils_obj:
    sql_data = pd.read_sql(f"select * from {LOGIN_TABLE},{EXPENSES_TABLE},{INVESTMENTS_TABLE},{INCOME_TABLE},{BANK_ACCOUNT_TABLE},{USER_TABLE} where username = 'priyav' and id = 1",utils_obj.conn)
print(sql_data)