from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.table_names import INCOME_TABLE, BANK_ACCOUNT_TABLE
from expense_manager.constants.exception_constants import BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR
from expense_manager.constants.success_constants import INCOME_ADDED_SUCCESSFULLY
from expense_manager.controller.bank_controller import is_bank_name_exist, balance


class IncomeController:
    def __init__(self):
        self.dbutils_obj = DbUtils()

    def is_income_already_exist(self, bank_name, id, source, amount, date, description):
        income_list = self.dbutils_obj.select_from_table(
            table_name=INCOME_TABLE,
            where_clause=f"bank_name = '{bank_name}' and id = {id} and source = '{source}' and amount = {amount} and date = {date} and description = '{description}'",
        )
        if income_list:
            return True
        else:
            return False

    def income_details(self, bank_name, id, source, amount, date, description):
        # if self.is_income_already_exist(bank_name, id, source, amount, date, description):
        #     return INCOME_RECORD_ALREADY_EXISTS_ERROR
        if not is_bank_name_exist(id, bank_name):
            return BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR
        self.dbutils_obj.insert_into_table(
            table_name=INCOME_TABLE,
            column_names="bank_name, id, source, amount, date, description",
            values=f"'{bank_name}',{id},'{source}',{amount},{date},'{description}'",
        )
        money_in_bank = balance(id=id, bank_name=bank_name) + amount
        self.dbutils_obj.update_in_table(
            table_name=BANK_ACCOUNT_TABLE,
            column_name="amount",
            value=money_in_bank,
            where_clause=f"id = {id} and bank_name = '{bank_name}'",
        )
        return INCOME_ADDED_SUCCESSFULLY


if __name__ == "__main__":
    income_control = IncomeController()
    print(
        income_control.income_details(
            bank_name="AXIS",
            id=1,
            source="Salary",
            amount=75000,
            date="2022-08-30",
            description="Salary for August",
        )
    )
