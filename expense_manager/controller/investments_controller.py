from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.table_names import BANK_ACCOUNT_TABLE, INVESTMENTS_TABLE
from expense_manager.constants.exception_constants import BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR
from expense_manager.constants.success_constants import INVESTMENTS_ADDED_SUCCESSFULLY
from expense_manager.controller.bank_controller import is_bank_name_exist, balance


class InvestmentsController:
    def __init__(self):
        self.dbutils_obj = DbUtils()

    def is_investments_already_exist(self, bank_name, id, type, amount, date, description):
        expense_list = self.dbutils_obj.select_from_table(
            table_name=INVESTMENTS_TABLE,
            where_clause=f"bank_name = '{bank_name}' and id = {id} and type = '{type}' and amount = {amount} and date = {date} and description = '{description}'",
        )
        if expense_list:
            return True
        else:
            return False

    # def is_sufficient_balance(self, bank_name, id, type, amount, date):
    #     money_in_bank = BankController().balance(id=id, bank_name=bank_name)
    #     if amount > money_in_bank:
    #         return False
    #     else:
    #         return True

    def investments_details(self, bank_name, id, type, amount, date, description):
        # if self.is_investments_already_exist(bank_name, id, type, amount, date, description):
        #     return INVESTMENTS_RECORD_ALREADY_EXISTS_ERROR
        if not is_bank_name_exist(id, bank_name):
            return BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR
        # if not self.is_sufficient_balance(bank_name, id, type, amount, date):
        #     return INSUFFICIENT_BALANCE
        self.dbutils_obj.insert_into_table(
            table_name=INVESTMENTS_TABLE,
            column_names="bank_name, id, type, amount, date, description",
            values=f"'{bank_name}',{id},'{type}',{amount},{date},'{description}'",
        )
        money_in_bank = balance(id=id, bank_name=bank_name) - amount
        self.dbutils_obj.update_in_table(
            table_name=BANK_ACCOUNT_TABLE,
            column_name="amount",
            value=money_in_bank,
            where_clause=f"id = {id} and bank_name = '{bank_name}'",
        )
        return INVESTMENTS_ADDED_SUCCESSFULLY


if __name__ == "__main__":
    investments_control = InvestmentsController()
    # print(investments_control.investments_details(bank_name="AXIS", id=1, type = "Mutual Funds", amount=900100, date="2022-08-30",
    #                                         description="Mutual Funds Zerodha"))
