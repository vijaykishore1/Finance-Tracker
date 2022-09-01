from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.table_names import (
    BANK_ACCOUNT_TABLE,
    INVESTMENTS_TABLE,
    INVESTMENTS_CATEGORY_TABLE,
)
from expense_manager.constants.exception_constants import BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR
from expense_manager.constants.success_constants import INVESTMENTS_ADDED_SUCCESSFULLY
from expense_manager.controller.bank_controller import BankController
from expense_manager.controller.categories_controller import InvestmentsCategoriesController


class InvestmentsController:
    def __init__(self):
        pass

    # def is_investments_already_exist(self, bank_name, id, type, amount, date, description):
    #     expense_list = self.dbutils_obj.select_from_table(
    #         table_name=INVESTMENTS_TABLE,
    #         where_clause=f"bank_name = '{bank_name}' and id = {id} and type = '{type}' and amount = {amount} and date = {date} and description = '{description}'",
    #     )
    #     if expense_list:
    #         return True
    #     else:
    #         return False

    # def is_sufficient_balance(self, bank_name, id, type, amount, date):
    #     money_in_bank = BankController().balance(id=id, bank_name=bank_name)
    #     if amount > money_in_bank:
    #         return False
    #     else:
    #         return True
    @staticmethod
    def insert_investments_details(
        bank_name, username, category, amount, date, description, sub_category=None
    ):
        # if self.is_investments_already_exist(bank_name, id, category_id, amount, date):
        #     return investments_RECORD_ALREADY_EXISTS_ERROR
        # if not self.is_sufficient_balance(bank_name, id, category_id, amount, date):
        #     return INSUFFICIENT_BALANCE
        if not BankController.is_bank_account_exist(username, bank_name):
            return BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR
        with DbUtils() as utils_obj:
            if InvestmentsCategoriesController.is_category_exists(category):
                if InvestmentsCategoriesController.is_sub_category_exists(sub_category):
                    new_category_id = utils_obj.select_from_table(
                        table_name=INVESTMENTS_CATEGORY_TABLE,
                        column_name="investments_category_id",
                        where_clause=f"investments_category = '{category}' and investments_sub_category = '{sub_category}'",
                    )[0][0]
                elif InvestmentsCategoriesController.is_sub_category_exists(category):
                    if not sub_category:
                        new_category_id = utils_obj.select_from_table(
                            table_name=INVESTMENTS_CATEGORY_TABLE,
                            column_name="investments_category_id",
                            where_clause=f"investments_sub_category = '{category}'",
                        )[0][0]
                elif not InvestmentsCategoriesController.is_sub_category_exists(sub_category):
                    utils_obj.insert_into_table(
                        table_name=INVESTMENTS_CATEGORY_TABLE,
                        column_names="investments_category, investments_sub_category",
                        values=f"'{category}','{sub_category}'",
                    )
                    new_category_id = utils_obj.select_from_table(
                        table_name=INVESTMENTS_CATEGORY_TABLE,
                        column_name="investments_category_id",
                        where_clause=f"investments_category = '{category}' and investments_sub_category = '{sub_category}'",
                    )[0][0]

                else:
                    new_category_id = utils_obj.select_from_table(
                        table_name=INVESTMENTS_CATEGORY_TABLE,
                        column_name="investments_category_id",
                        where_clause=f"investments_category = '{category}'",
                    )[0][0]

            if not InvestmentsCategoriesController.is_category_exists(category):
                if not InvestmentsCategoriesController.is_sub_category_exists(sub_category):
                    if not InvestmentsCategoriesController.is_sub_category_exists(category):
                        if sub_category:
                            utils_obj.insert_into_table(
                                table_name=INVESTMENTS_CATEGORY_TABLE,
                                column_names="investments_category, investments_sub_category",
                                values=f"'{category}','{sub_category}'",
                            )
                            new_category_id = utils_obj.select_from_table(
                                table_name=INVESTMENTS_CATEGORY_TABLE,
                                column_name="investments_category_id",
                                where_clause=f"investments_category = '{category}' and investments_sub_category = '{sub_category}'",
                            )[0][0]
                        else:
                            utils_obj.insert_into_table(
                                table_name=INVESTMENTS_CATEGORY_TABLE,
                                column_names="investments_category",
                                values=f"'{category}'",
                            )
                            new_category_id = utils_obj.select_from_table(
                                table_name=INVESTMENTS_CATEGORY_TABLE,
                                column_name="investments_category_id",
                                where_clause=f"investments_category = '{category}'",
                            )[0][0]
                if InvestmentsCategoriesController.is_sub_category_exists(category):
                    new_category_id = utils_obj.select_from_table(
                        table_name=INVESTMENTS_CATEGORY_TABLE,
                        column_name="investments_category_id",
                        where_clause=f"investments_sub_category = '{category}'",
                    )[0][0]

            user_id = utils_obj.select_from_table(
                table_name="login", column_name="login_id", where_clause=f"username = '{username}'"
            )[0][0]
            utils_obj.insert_into_table(
                table_name=INVESTMENTS_TABLE,
                column_names="bank_name, id, investments_category_id, amount, date, description",
                values=f"'{bank_name}',{user_id},{new_category_id},{amount},'{date}','{description}'",
            )
            money_in_bank = (
                BankController.get_balance(username=username, bank_name=bank_name) - amount
            )
            utils_obj.update_in_table(
                table_name=BANK_ACCOUNT_TABLE,
                column_name="amount",
                value=money_in_bank,
                where_clause=f"id = {user_id} and bank_name = '{bank_name}'",
            )
        return INVESTMENTS_ADDED_SUCCESSFULLY


if __name__ == "__main__":
    print(
        InvestmentsController.insert_investments_details(
            bank_name="HSBC",
            username="abhijitashok",
            category="Mutual Funds",
            amount=9001,
            date="2022-08-30",
            description="Mutual Funds Zerodha",
        )
    )
