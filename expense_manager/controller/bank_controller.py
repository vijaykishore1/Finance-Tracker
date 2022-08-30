from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.table_names import BANK_ACCOUNT_TABLE
from expense_manager.constants.exception_constants import BANK_ACCOUNT_ALREADY_EXISTS_ERROR
from expense_manager.constants.success_constants import BANK_DETAILS_ADDED_SUCCESSFULLY


class BankController:
    def __init__(self):
        pass

    def balance(self, id, bank_name):
        balance = DbUtils().select_from_table(table_name=BANK_ACCOUNT_TABLE, column_name="amount",
                                              where_clause=f"id = {id} and bank_name = '{bank_name}'")[0][0]
        return balance

    def is_bank_name_exist(self, id, bank_name):
        bank_list = DbUtils().select_from_table(column_name="bank_name", table_name=BANK_ACCOUNT_TABLE,
                                                where_clause=f"bank_name = '{bank_name}' and id = {id}")
        if bank_list:
            return True
        else:
            return False

    def bank_details(self, id, bank_name, amount=0):
        if self.is_bank_name_exist(id, bank_name):
            return BANK_ACCOUNT_ALREADY_EXISTS_ERROR
        DbUtils().insert_into_table(table_name="bank_account", column_names="id, bank_name, amount",
                                    values=f"{id},'{bank_name}','{amount}'")
        return BANK_DETAILS_ADDED_SUCCESSFULLY


if __name__ == '__main__':
    bank_control = BankController()
    print(bank_control.bank_details(id=2, bank_name="AXIS", amount=10000))
    print(bank_control.balance(id=1, bank_name="AXIS"))
