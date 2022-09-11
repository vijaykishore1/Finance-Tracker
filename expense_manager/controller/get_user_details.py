from expense_manager.controller.login_controller import LoginController
from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.exception_constants import USERNAME_DOES_NOT_EXIST_ERROR
from expense_manager.constants.table_names import LOGIN_TABLE, EXPENSES_TABLE, EXPENSES_CATEGORY_TABLE, \
    INVESTMENTS_TABLE, INCOME_TABLE, BANK_ACCOUNT_TABLE, USER_TABLE, INVESTMENTS_CATEGORY_TABLE, INCOME_CATEGORY_TABLE


class GetDetails:
    @staticmethod
    def get_login_details_of_user(username):
        if not LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        with DbUtils() as utils_obj:
            query = f"select username from {LOGIN_TABLE} where username = '{username}' "
            res = (utils_obj.run_query(input_str=query))
            ans.append("username = " + res.fetchall()[0][0])
            query = f"select password from {LOGIN_TABLE} where username = '{username}' "
            res = (utils_obj.run_query(input_str=query))
            ans.append("password = " + res.fetchall()[0][0])
            query = f"select email from {LOGIN_TABLE} where username = '{username}' "
            res = (utils_obj.run_query(input_str=query))
            ans.append("email = " + res.fetchall()[0][0])
        for i in range(len(ans)):
            final_ans += ans[i] + "\n"
        return final_ans

    @staticmethod
    def get_bio_of_user(username):
        if not LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        with DbUtils() as utils_obj:
            user_id = \
                utils_obj.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                    0][
                    0]
            # utils_obj.get_login_details_of_user(username=username)
            query = f"select name from {USER_TABLE} where id = '{user_id}' "
            res = (utils_obj.run_query(input_str=query))
            ans.append("name = " + res.fetchall()[0][0])
            query = f"select phone_number from {USER_TABLE} where id = '{user_id}' "
            res = (utils_obj.run_query(input_str=query))
            ans.append("Phone Number = " + res.fetchall()[0][0])
        for i in range(len(ans)):
            final_ans += ans[i] + "\n"
        return final_ans

    @staticmethod
    def get_bank_accounts_of_user(username):
        if not LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        with DbUtils() as utils_obj:
            user_id = \
                utils_obj.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                    0][
                    0]
    
            query = f"select bank_name from {BANK_ACCOUNT_TABLE} where id = '{user_id}' "
            res = (utils_obj.run_query(input_str=query))
            bank_account_array = res.fetchall()
        for i in range(len(bank_account_array)):
            ans.append(f"Bank Account {i + 1} = {bank_account_array[i][0]}")
        for i in range(len(ans)):
            final_ans += ans[i] + "\n"
        return final_ans

    @staticmethod
    def get_income_details_of_user(username):
        if not LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        with DbUtils() as utils_obj:
            user_id = \
                utils_obj.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                    0][
                    0]
        
            income_array = utils_obj.select_from_table(table_name="income", column_name="amount",
                                                       where_clause=f"id = {user_id}")
            income_category_id_array = utils_obj.select_from_table(table_name="income",
                                                                   column_name="income_category_id",
                                                                   where_clause=f"id = {user_id}")
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
                                                            where_clause=f"id = {user_id}")
            for i in range(len(income_array)):
                if not income_sub_category_array[i][0][0]:
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

    @staticmethod
    def get_investments_details_of_user(username):
        if not LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        with DbUtils() as utils_obj:
            user_id = \
                utils_obj.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                    0][
                    0]

            investments_array = utils_obj.select_from_table(table_name="investments", column_name="amount",
                                                            where_clause=f"id = {user_id}")
            investments_category_id_array = utils_obj.select_from_table(table_name="investments",
                                                                        column_name="investments_category_id",
                                                                        where_clause=f"id = {user_id}")
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
                                                                 where_clause=f"id = {user_id}")
            for i in range(len(investments_array)):
                if not investments_sub_category_array[i][0][0]:
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

    @staticmethod
    def get_expenses_details_of_user(username):
        if not LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        ans = []
        final_ans = ""
        with DbUtils() as utils_obj:
            user_id = \
                utils_obj.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                    0][
                    0]

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
                if not expenses_sub_category_array[i][0][0]:
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

    @staticmethod
    def get_balance_of_user(username):
        if not LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        with DbUtils() as utils_obj:
            user_id = \
                utils_obj.select_from_table(table_name="login", column_name="login_id", where_clause=f"username = '{username}'")[
                    0][
                    0]
            ans = []
            final_ans = ""
            query = f"select bank_name from {BANK_ACCOUNT_TABLE} where id = '{user_id}' "
            res = (utils_obj.run_query(input_str=query))
            bank_account_array = res.fetchall()
            query = f"select amount from {BANK_ACCOUNT_TABLE} where id = '{user_id}' "
            res = (utils_obj.run_query(input_str=query))
            balance_in_account_array = res.fetchall()
            # print("balances are:", balance_in_account_array[2][0])
        for i in range(len(bank_account_array)):
            ans.append(f"Balance in {bank_account_array[i][0]}= {str(balance_in_account_array[i][0])}")
        for i in range(len(ans)):
            final_ans += ans[i] + "\n"
        return final_ans

    @staticmethod
    def get_all_details_of_user(username):
        if not LoginController.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        
        final_ans = GetDetails.get_login_details_of_user(username=username) + GetDetails.get_bio_of_user(
            username=username) + GetDetails.get_bank_accounts_of_user(username=username) + GetDetails.get_balance_of_user(
            username=username) + GetDetails.get_income_details_of_user(username=username) + GetDetails.get_expenses_details_of_user(
            username=username) + GetDetails.get_investments_details_of_user(username=username)
        return final_ans


if __name__ == '__main__':
    # print(utils_obj.get_all_details_of_user(username="abhijitashok"))
    # print(utils_obj.get_balance_of_user(username="abhijitashok"))
    print(GetDetails.get_login_details_of_user(username="abhijitashok"))
    # print(utils_obj.get_bio_of_user(username="abhijitashok"))
    # print(utils_obj.get_bank_accounts_of_user(username="abhijitashok"))
    # print(utils_obj.get_balance_of_user(username="abhijitashok"))
    # print(utils_obj.get_income_details_of_user(username="abhijitashok"))
    # print(utils_obj.get_investments_details_of_user(username="abhijitashok"))
    # print(utils_obj.get_expenses_details_of_user(username="abhijitashok"))
    # print(utils_obj.get_all_details_of_user(username="priyav"))
