import sqlite3
# import finance_tracker.controller.login_controller
from finance_tracker.constants.db_constants import DB_PATH
from finance_tracker.constants.table_names import LOGIN_TABLE, EXPENSES_TABLE, EXPENSES_CATEGORY_TABLE, \
    INCOME_CATEGORY_TABLE, INVESTMENTS_CATEGORY_TABLE, INVESTMENTS_TABLE, INCOME_TABLE, BANK_ACCOUNT_TABLE, USER_TABLE
from finance_tracker.constants.exception_constants import USERNAME_DOES_NOT_EXIST_ERROR


class DbUtils:
    def __init__(self):
        self.database = DB_PATH
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.database)
        return self

    def run_query(
            self,
            input_str,
    ):
        # print(
        #     "Executing input_str:",
        #     input_str,
        # )
        cur = self.conn.cursor()
        cur.execute(input_str)
        self.conn.commit()
        return cur

    # def insert_into_table(
    #     self,
    #     table_name,
    #     values,
    # ):
    #     query = f"insert into {table_name} values ({values})"
    #     self.run_query(input_str=query)
    #     print("Record inserted successfully")
    def insert_into_table(self, table_name, column_names, values):
        query = f"insert into {table_name} ({column_names}) values ({values})"
        self.run_query(input_str=query)
        print("Values inserted successfully")

    def update_in_table(self, table_name, column_name, value, where_clause=""):
        query = f"update {table_name} set {column_name} = '{value}'"
        if where_clause:
            query += f" where {where_clause}"
        self.run_query(input_str=query)
        print("Table updated successfully")

    def select_from_table(self, table_name, column_name="*", where_clause=""):
        query = f"select {column_name} from {table_name}"
        if where_clause:
            query += f" where {where_clause}"
        res = self.run_query(input_str=query)
        return res.fetchall()

    def delete_from_table(self, table_name, where_clause=""):
        query = f"delete from {table_name}"
        if where_clause:
            query += f" where {where_clause}"
        self.run_query(input_str=query)
        print("Record deleted successfully")

    @staticmethod
    def is_value_match(value1, value2):
        if value1 != value2:
            return False
        else:
            return True

    def alter_the_column_name(
            self, table_name, old_name, new_name
    ):  # BE CAREFUL WITH THIS METHOD AND USE IT
        # ONLY FOR IMPORTANT OPERATIONS
        query = f"alter table '{table_name}' rename column '{old_name}' to '{new_name}'"
        self.run_query(input_str=query)
        print("Column Name Changed Successfully")

    def alter_add_a_column_to_table(
            self, table_name, column_name
    ):  # BE CAREFUL WITH THIS METHOD AND USE IT ONLY FOR IMPORTANT OPERATIONS
        query = f"alter table '{table_name}' add '{column_name}' INT not null default(0)"
        self.run_query(input_str=query)
        print("Column Added Successfully")

    def drop_table(
            self, table_name
    ):  # BE CAREFUL WITH THIS METHOD AND USE IT ONLY FOR IMPORTANT OPERATIONS
        query = f"drop table {table_name}"
        self.run_query(input_str=query)
        print("Table deleted successfully")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()


if __name__ == "__main__":
    with DbUtils() as utils_obj:
        # utils_obj.delete_from_table(table_name="expenses_categories",where_clause='expenses_category_id = 3')

        # utils_obj.delete_from_table(table_name=USER_TABLE)
        # utils_obj.delete_from_table(table_name=LOGIN_TABLE)
        # utils_obj.delete_from_table(table_name=INCOME_CATEGORY_TABLE)
        # utils_obj.delete_from_table(table_name=INVESTMENTS_TABLE)
        # utils_obj.delete_from_table(table_name=EXPENSES_CATEGORY_TABLE)
        # utils_obj.delete_from_table(table_name=EXPENSES_TABLE)
        # utils_obj.delete_from_table(table_name=INCOME_TABLE)
        # utils_obj.delete_from_table(table_name=INVESTMENTS_TABLE)
        # utils_obj.delete_from_table(table_name=BANK_ACCOUNT_TABLE)

        # utils_obj.drop_table(table_name=LOGIN_TABLE)
        # utils_obj.drop_table(table_name=INVESTMENTS_TABLE)
        # utils_obj.drop_table(table_name=INCOME_TABLE)
        # utils_obj.drop_table(table_name=EXPENSES_TABLE)
        # utils_obj.drop_table(table_name=INVESTMENTS_CATEGORY_TABLE)
        # utils_obj.drop_table(table_name=INCOME_CATEGORY_TABLE)
        # utils_obj.drop_table(table_name=EXPENSES_CATEGORY_TABLE)

        # utils_obj.update_in_table(table_name=LOGIN_TABLE,column_name='email',value='abhijitashok123@gmail.com')

        # print(utils_obj.select_from_table(table_name="user"))
        print(utils_obj.select_from_table(table_name="login"))
        # print(utils_obj.select_from_table(table_name="bank_account"))
        # # print(utils_obj.select_from_table(table_name=BANK_ACCOUNT_TABLE, column_name="bank_name", where_clause="id = 1"))
        # print(utils_obj.select_from_table(table_name="income", column_name="amount", where_clause="id = 1"))
        # print(utils_obj.select_from_table(table_name="expenses"))
        # print(utils_obj.select_from_table(table_name="investments"))
        # print(utils_obj.select_from_table(table_name="investments_categories"))
        # print(utils_obj.select_from_table(table_name="expenses_categories"))
        # print(utils_obj.select_from_table(table_name="income_categories"))
