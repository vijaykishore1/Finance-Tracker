import sqlite3
import expense_manager.controller.login_controller
from expense_manager.constants.db_constants import DB_PATH
from expense_manager.constants.table_names import LOGIN_TABLE, EXPENSES_TABLE, EXPENSES_CATEGORY_TABLE, \
    INCOME_CATEGORY_TABLE, INVESTMENTS_CATEGORY_TABLE, INVESTMENTS_TABLE, INCOME_TABLE, BANK_ACCOUNT_TABLE, USER_TABLE
from expense_manager.constants.exception_constants import USERNAME_DOES_NOT_EXIST_ERROR


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

    def update_in_table_interactive(
            self,
            table_name,
    ):
        no_of_updates = int(input("how many values do you want to update"))
        list_column = []
        list_value = []
        for i in range(no_of_updates):
            list_column.append(input("Enter column to update:"))
            list_value.append(input("Enter new value to update:"))
        check_column = input("Enter column for condition check:")
        check_value = input("Enter value for condition check:")
        for i in range(no_of_updates):
            query = f"update {table_name} set {list_column[i]} = '{list_value[i]}' where {check_column} = {check_value}"
            self.run_query(input_str=query)
        print("Table updated successfully")

    def update_in_table(self, table_name, column_name, value, where_clause=""):
        query = f"update {table_name} set {column_name} = '{value}'"
        if where_clause:
            query += f" where {where_clause}"
        self.run_query(input_str=query)
        print("Table updated successfully")

    def get_login_details_of_user(self, username):
        if not expense_manager.controller.login_controller.LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        query = f"select username from {LOGIN_TABLE} where username = '{username}' "
        res = (self.run_query(input_str=query))
        ans.append("username = " + res.fetchall()[0][0])
        query = f"select password from {LOGIN_TABLE} where username = '{username}' "
        res = (self.run_query(input_str=query))
        ans.append("password = " + res.fetchall()[0][0])
        for i in range(len(ans)):
            final_ans += ans[i] + "\n"
        return final_ans

    def get_bio_of_user(self, username):
        if not expense_manager.controller.login_controller.LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        user_id = \
            self.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                0][
                0]
        self.get_login_details_of_user(username=username)
        query = f"select name from {USER_TABLE} where id = '{user_id}' "
        res = (self.run_query(input_str=query))
        ans.append("name = " + res.fetchall()[0][0])
        query = f"select phone_number from {USER_TABLE} where id = '{user_id}' "
        res = (self.run_query(input_str=query))
        ans.append("Phone Number = " + res.fetchall()[0][0])
        for i in range(len(ans)):
            final_ans += ans[i] + "\n"
        return final_ans

    def get_bank_accounts_of_user(self, username):
        if not expense_manager.controller.login_controller.LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        user_id = \
            self.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                0][
                0]

        query = f"select bank_name from {BANK_ACCOUNT_TABLE} where id = '{user_id}' "
        res = (self.run_query(input_str=query))
        bank_account_array = res.fetchall()
        for i in range(len(bank_account_array)):
            ans.append(f"Bank Account {i + 1} = {bank_account_array[i][0]}")
        for i in range(len(ans)):
            final_ans += ans[i] + "\n"
        return final_ans

    def get_income_details_of_user(self, username):
        if not expense_manager.controller.login_controller.LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        user_id = \
            self.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                0][
                0]
        with DbUtils() as utils_obj:
            income_array = utils_obj.select_from_table(table_name="income", column_name="amount",
                                                       where_clause=f"id = {user_id}")
            income_category_id_array = utils_obj.select_from_table(table_name="income",
                                                                   column_name="income_category_id",
                                                                   where_clause="id = 1")
            income_category_array = []
            income_sub_category_array = []
            for i in range(len(income_category_id_array)):
                income_category_array.append(
                    utils_obj.select_from_table(table_name="income_categories", column_name="income_category",
                                                where_clause=f"income_category_id = {income_category_id_array[i][0]}"))
            # print(income_category_array)
            for i in range(len(income_category_id_array)):
                income_sub_category_array.append(
                    utils_obj.select_from_table(table_name="income_categories", column_name="income_sub_category",
                                                where_clause=f"income_category_id = {income_category_id_array[i][0]}"))
            # print(income_sub_category_array)
            income_date_array = utils_obj.select_from_table(table_name="income", column_name="date",
                                                            where_clause="id = 1")
            for i in range(len(income_array)):
                if income_sub_category_array[i][0][0] == None:
                    ans.append(
                        f"You have earned {income_array[i][0]} from {income_category_array[i][0][0]} on {income_date_array[i][0]}")
                else:
                    ans.append(
                        f"You have earned {income_array[i][0]} from {income_category_array[i][0][0]},{income_sub_category_array[i][0][0]} on {income_date_array[i][0]}")

            for i in range(len(ans)):
                final_ans += ans[i] + "\n"
        if len(ans) == 0:
            return "you don't have any income record yet \n"
        return final_ans

    def get_investments_details_of_user(self, username):
        if not expense_manager.controller.login_controller.LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        user_id = \
            self.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                0][
                0]
        with DbUtils() as utils_obj:
            investments_array = utils_obj.select_from_table(table_name="investments", column_name="amount",
                                                            where_clause=f"id = {user_id}")
            investments_category_id_array = utils_obj.select_from_table(table_name="investments",
                                                                        column_name="investments_category_id",
                                                                        where_clause="id = 1")
            investments_category_array = []
            investments_sub_category_array = []
            for i in range(len(investments_category_id_array)):
                investments_category_array.append(
                    utils_obj.select_from_table(table_name="investments_categories", column_name="investments_category",
                                                where_clause=f"investments_category_id = {investments_category_id_array[i][0]}"))
            # print(investments_category_array)
            for i in range(len(investments_category_id_array)):
                investments_sub_category_array.append(
                    utils_obj.select_from_table(table_name="investments_categories",
                                                column_name="investments_sub_category",
                                                where_clause=f"investments_category_id = {investments_category_id_array[i][0]}"))
            # print(investments_sub_category_array)
            investments_date_array = utils_obj.select_from_table(table_name="investments", column_name="date",
                                                                 where_clause="id = 1")
            for i in range(len(investments_array)):
                if investments_sub_category_array[i][0][0] == None:
                    ans.append(
                        f"You have invested {investments_array[i][0]} in {investments_category_array[i][0][0]} on {investments_date_array[i][0]}")
                else:
                    ans.append(
                        f"You have invested {investments_array[i][0]} in {investments_category_array[i][0][0]},{investments_sub_category_array[i][0][0]} on {investments_date_array[i][0]}")

            for i in range(len(ans)):
                final_ans += ans[i] + "\n"
        if len(ans) == 0:
            return "you haven't made any investments \n"
        return final_ans

    def get_expenses_details_of_user(self, username):
        if not expense_manager.controller.login_controller.LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        user_id = \
            self.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                0][
                0]
        with DbUtils() as utils_obj:
            expenses_array = utils_obj.select_from_table(table_name="expenses", column_name="amount",
                                                         where_clause=f"id = {user_id}")
            # print(expenses_array)
            expenses_category_id_array = utils_obj.select_from_table(table_name="expenses",
                                                                     column_name="expenses_category_id",
                                                                     where_clause=f"id = {user_id}")
            expenses_category_array = []
            expenses_sub_category_array = []
            for i in range(len(expenses_category_id_array)):
                expenses_category_array.append(
                    utils_obj.select_from_table(table_name="expenses_categories", column_name="expenses_category",
                                                where_clause=f"expenses_category_id = {expenses_category_id_array[i][0]}"))
            # print(expenses_category_array)
            for i in range(len(expenses_category_id_array)):
                expenses_sub_category_array.append(
                    utils_obj.select_from_table(table_name="expenses_categories", column_name="expenses_sub_category",
                                                where_clause=f"expenses_category_id = {expenses_category_id_array[i][0]}"))
            # print(expenses_sub_category_array)
            expenses_date_array = utils_obj.select_from_table(table_name="expenses", column_name="date",
                                                              where_clause=f"id = {user_id}")
            # print(len(expenses_array))
            for i in range(len(expenses_array)):
                if expenses_sub_category_array[i][0][0] == None:
                    ans.append(
                        f"You have spent {expenses_array[i][0]} for {expenses_category_array[i][0][0]} on {expenses_date_array[i][0]}")
                else:
                    ans.append(
                        f"You have spent {expenses_array[i][0]} for {expenses_category_array[i][0][0]},{expenses_sub_category_array[i][0][0]} on {expenses_date_array[i][0]}")

            for i in range(len(ans)):
                final_ans += ans[i] + "\n"
        if len(ans) == 0:
            return "you haven't made any expenses \n"
        return final_ans

    def get_balance_of_user(self, username):
        if not expense_manager.controller.login_controller.LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        user_id = \
            self.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                0][
                0]
        ans = []
        final_ans = ""
        query = f"select bank_name from {BANK_ACCOUNT_TABLE} where id = '{user_id}' "
        res = (self.run_query(input_str=query))
        bank_account_array = res.fetchall()
        query = f"select amount from {BANK_ACCOUNT_TABLE} where id = '{user_id}' "
        res = (self.run_query(input_str=query))
        balance_in_account_array = res.fetchall()
        # print("balances are:", balance_in_account_array[2][0])
        for i in range(len(bank_account_array)):
            ans.append(f"Balance in {bank_account_array[i][0]}= {str(balance_in_account_array[i][0])}")
        for i in range(len(ans)):
            final_ans += ans[i] + "\n"
        return final_ans

    def get_all_details_of_user(self, username):
        if not expense_manager.controller.login_controller.LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        final_ans = self.get_login_details_of_user(username=username)+ self.get_bio_of_user(
            username=username) + self.get_bank_accounts_of_user(username=username) + self.get_balance_of_user(
            username=username) + self.get_income_details_of_user(username=username) + self.get_expenses_details_of_user(
            username=username) + self.get_investments_details_of_user(username=username)
        return final_ans

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
        # utils_obj.delete_from_table(table_name="income")
        # utils_obj.delete_from_table(table_name="expenses")
        # utils_obj.drop_table(table_name=INVESTMENTS_TABLE)
        # utils_obj.drop_table(table_name=INCOME_TABLE)
        # utils_obj.drop_table(table_name=EXPENSES_TABLE)
        # utils_obj.drop_table(table_name=INVESTMENTS_CATEGORY_TABLE)
        # utils_obj.drop_table(table_name=INCOME_CATEGORY_TABLE)
        # utils_obj.drop_table(table_name=EXPENSES_CATEGORY_TABLE)
        # utils_obj.update_in_table(table_name="bank_account",column_name="amount",value=100000)

        # print(utils_obj.select_from_table(table_name="user"))
        # print(utils_obj.select_from_table(table_name="login"))
        # print(utils_obj.select_from_table(table_name="bank_account"))
        # # print(utils_obj.select_from_table(table_name=BANK_ACCOUNT_TABLE, column_name="bank_name", where_clause="id = 1"))
        # print(utils_obj.select_from_table(table_name="income", column_name="amount", where_clause="id = 1"))
        # print(utils_obj.select_from_table(table_name="expenses"))
        # print(utils_obj.select_from_table(table_name="investments"))
        # print(utils_obj.select_from_table(table_name="investments_categories"))
        # print(utils_obj.select_from_table(table_name="expenses_categories"))
        # print(utils_obj.select_from_table(table_name="income_categories"))

        # print(utils_obj.get_all_details_of_user(username="abhijitashok"))
        # print(utils_obj.get_balance_of_user(username="abhijitashok"))
        # print(utils_obj.get_login_details_of_user(username="abhijitashok"))
        # print(utils_obj.get_bio_of_user(username="abhijitashok"))
        # print(utils_obj.get_bank_accounts_of_user(username="abhijitashok"))
        # print(utils_obj.get_balance_of_user(username="abhijitashok"))
        # print(utils_obj.get_income_details_of_user(username="abhijitashok"))
        # print(utils_obj.get_investments_details_of_user(username="abhijitashok"))
        # print(utils_obj.get_expenses_details_of_user(username="abhijitashok"))
        print(utils_obj.get_all_details_of_user(username="priyav"))
