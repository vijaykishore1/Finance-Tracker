from finance_tracker.db.db_utils import DbUtils
from finance_tracker.constants.table_names import USER_TABLE, BANK_ACCOUNT_TABLE, LOGIN_TABLE
from finance_tracker.constants.exception_constants import BANK_ACCOUNT_ALREADY_EXISTS_ERROR
from finance_tracker.constants.success_constants import BANK_DETAILS_ADDED_SUCCESSFULLY
from finance_tracker.controller.login_controller import LoginController


class BankController:
    def __init__(self):
        pass

    @staticmethod
    def is_bank_account_exist(username, bank_name):
        with DbUtils() as utils_obj:
            user_id = utils_obj.select_from_table(
                table_name="login", column_name="login_id", where_clause=f"username = '{username}'"
            )[0][0]
            bank_list = utils_obj.select_from_table(
                table_name="bank_account,login",
                column_name="bank_name",
                where_clause=f"bank_name = '{bank_name}' and id = {user_id}",
            )
        if bank_list:
            return True
        else:
            return False

    @staticmethod
    def insert_bank_details(username, bank_name, amount=0):
        if BankController.is_bank_account_exist(username, bank_name):
            return BANK_ACCOUNT_ALREADY_EXISTS_ERROR
        with DbUtils() as utils_obj:
            user_id = utils_obj.select_from_table(
                table_name="login", column_name="login_id", where_clause=f"username = '{username}'"
            )[0][0]
            print(user_id)
            utils_obj.insert_into_table(
                table_name=BANK_ACCOUNT_TABLE,
                column_names="id, bank_name, amount",
                values=f"{user_id},'{bank_name}','{amount}'",
            )
        return BANK_DETAILS_ADDED_SUCCESSFULLY

    @staticmethod
    def get_balance(username, bank_name):
        with DbUtils() as utils_obj:
            user_id = utils_obj.select_from_table(
                table_name="login", column_name="login_id", where_clause=f"username = '{username}'"
            )[0][0]
            balances = utils_obj.select_from_table(
                table_name=BANK_ACCOUNT_TABLE,
                column_name="amount",
                where_clause=f"id = '{user_id}' and bank_name = '{bank_name}'",
            )[0][0]
        return balances


if __name__ == "__main__":
    bank_control = BankController()
    # print(BankController.insert_bank_details(username="priyav", bank_name="HSBC", amount=10000))
    print(bank_control.get_balance(username="priyav", bank_name="HSBC"))
