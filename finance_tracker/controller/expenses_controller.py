from finance_tracker.db.db_utils import DbUtils
from finance_tracker.constants.table_names import (
    BANK_ACCOUNT_TABLE,
    EXPENSES_TABLE,
    EXPENSES_CATEGORY_TABLE,
)
from finance_tracker.constants.exception_constants import BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR
from finance_tracker.constants.success_constants import EXPENSES_ADDED_SUCCESSFULLY
from finance_tracker.controller.bank_controller import BankController
from finance_tracker.controller.categories_controller import ExpensesCategoriesController


class ExpensesController:
    def __init__(self):
        pass

    # def is_expenses_already_exist(self, bank_name, id, category_id, amount, date):
    #     expense_list = self.dbutils_obj.select_from_table(
    #         table_name=EXPENSES_TABLE,
    #         where_clause=f"bank_name = '{bank_name}' and id = {id} and category_id = {category_id} and amount = {amount} and date = {date}",
    #     )
    #     if expense_list:
    #         return True
    #     else:
    #         return False

    # def is_sufficient_balance(self, bank_name, id, category_id, amount, date):
    #     money_in_bank = BankController().balance(id=id, bank_name=bank_name)
    #     if amount > money_in_bank:
    #         return False
    #     else:
    #         return True
    @staticmethod
    def insert_expenses_details(
        bank_name, username, category, amount, date, description, sub_category=None
    ):
        # if self.is_expenses_already_exist(bank_name, id, category_id, amount, date):
        #     return expenses_RECORD_ALREADY_EXISTS_ERROR
        # if not self.is_sufficient_balance(bank_name, id, category_id, amount, date):
        #     return INSUFFICIENT_BALANCE
        if not BankController.is_bank_account_exist(username, bank_name):
            return BANK_ACCOUNT_DOES_NOT_EXISTS_ERROR
        with DbUtils() as utils_obj:
            if ExpensesCategoriesController.is_category_exists(category):
                if ExpensesCategoriesController.is_sub_category_exists(sub_category):
                    new_category_id = utils_obj.select_from_table(
                        table_name=EXPENSES_CATEGORY_TABLE,
                        column_name="expenses_category_id",
                        where_clause=f"expenses_category = '{category}' and expenses_sub_category = '{sub_category}'",
                    )[0][0]
                    count_of_this_category = (
                        utils_obj.select_from_table(
                            table_name=EXPENSES_CATEGORY_TABLE,
                            column_name="count",
                            where_clause=f"expenses_category = '{category}' and expenses_sub_category = '{sub_category}'",
                        )[0][0]
                        + 1
                    )
                    utils_obj.update_in_table(
                        table_name=EXPENSES_CATEGORY_TABLE,
                        column_name="count",
                        value=count_of_this_category,
                        where_clause=f"expenses_category = '{category}' and expenses_sub_category = '{sub_category}'",
                    )
                elif ExpensesCategoriesController.is_sub_category_exists(category):
                    if not sub_category:
                        new_category_id = utils_obj.select_from_table(
                            table_name=EXPENSES_CATEGORY_TABLE,
                            column_name="expenses_category_id",
                            where_clause=f"expenses_sub_category = '{category}'",
                        )[0][0]
                        count_of_this_category = (
                            utils_obj.select_from_table(
                                table_name=EXPENSES_CATEGORY_TABLE,
                                column_name="count",
                                where_clause=f"expenses_sub_category = '{category}'",
                            )[0][0]
                            + 1
                        )
                        utils_obj.update_in_table(
                            table_name=EXPENSES_CATEGORY_TABLE,
                            column_name="count",
                            value=count_of_this_category,
                            where_clause=f"expenses_sub_category = '{category}'",
                        )
                elif not ExpensesCategoriesController.is_sub_category_exists(sub_category):
                    utils_obj.insert_into_table(
                        table_name=EXPENSES_CATEGORY_TABLE,
                        column_names="expenses_category, expenses_sub_category",
                        values=f"'{category}','{sub_category}'",
                    )
                    new_category_id = utils_obj.select_from_table(
                        table_name=EXPENSES_CATEGORY_TABLE,
                        column_name="expenses_category_id",
                        where_clause=f"expenses_category = '{category}' and expenses_sub_category = '{sub_category}'",
                    )[0][0]
                    count_of_this_category = (
                        utils_obj.select_from_table(
                            table_name=EXPENSES_CATEGORY_TABLE,
                            column_name="count",
                            where_clause=f"expenses_category = '{category}' and expenses_sub_category = '{sub_category}'",
                        )[0][0]
                        + 1
                    )
                    utils_obj.update_in_table(
                        table_name=EXPENSES_CATEGORY_TABLE,
                        column_name="count",
                        value=count_of_this_category,
                        where_clause=f"expenses_category = '{category}' and expenses_sub_category = '{sub_category}'",
                    )

                else:
                    new_category_id = utils_obj.select_from_table(
                        table_name=EXPENSES_CATEGORY_TABLE,
                        column_name="expenses_category_id",
                        where_clause=f"expenses_category = '{category}'",
                    )[0][0]
                    count_of_this_category = (
                        utils_obj.select_from_table(
                            table_name=EXPENSES_CATEGORY_TABLE,
                            column_name="count",
                            where_clause=f"expenses_category = '{category}'",
                        )[0][0]
                        + 1
                    )
                    utils_obj.update_in_table(
                        table_name=EXPENSES_CATEGORY_TABLE,
                        column_name="count",
                        value=count_of_this_category,
                        where_clause=f"expenses_category = '{category}'",
                    )
            if not ExpensesCategoriesController.is_category_exists(category):
                if not ExpensesCategoriesController.is_sub_category_exists(sub_category):
                    if not ExpensesCategoriesController.is_sub_category_exists(category):
                        if sub_category:
                            utils_obj.insert_into_table(
                                table_name=EXPENSES_CATEGORY_TABLE,
                                column_names="expenses_category, expenses_sub_category",
                                values=f"'{category}','{sub_category}'",
                            )
                            new_category_id = utils_obj.select_from_table(
                                table_name=EXPENSES_CATEGORY_TABLE,
                                column_name="expenses_category_id",
                                where_clause=f"expenses_category = '{category}' and expenses_sub_category = '{sub_category}'",
                            )[0][0]
                            count_of_this_category = (
                                utils_obj.select_from_table(
                                    table_name=EXPENSES_CATEGORY_TABLE,
                                    column_name="count",
                                    where_clause=f"expenses_category = '{category}' and expenses_sub_category = '{sub_category}'",
                                )[0][0]
                                + 1
                            )
                            utils_obj.update_in_table(
                                table_name=EXPENSES_CATEGORY_TABLE,
                                column_name="count",
                                value=count_of_this_category,
                                where_clause=f"expenses_category = '{category}' and expenses_sub_category = '{sub_category}'",
                            )
                        else:
                            utils_obj.insert_into_table(
                                table_name=EXPENSES_CATEGORY_TABLE,
                                column_names="expenses_category",
                                values=f"'{category}'",
                            )
                            new_category_id = utils_obj.select_from_table(
                                table_name=EXPENSES_CATEGORY_TABLE,
                                column_name="expenses_category_id",
                                where_clause=f"expenses_category = '{category}'",
                            )[0][0]
                            count_of_this_category = (
                                utils_obj.select_from_table(
                                    table_name=EXPENSES_CATEGORY_TABLE,
                                    column_name="count",
                                    where_clause=f"expenses_category = '{category}'",
                                )[0][0]
                                + 1
                            )
                            utils_obj.update_in_table(
                                table_name=EXPENSES_CATEGORY_TABLE,
                                column_name="count",
                                value=count_of_this_category,
                                where_clause=f"expenses_category = '{category}'",
                            )
                if ExpensesCategoriesController.is_sub_category_exists(category):
                    new_category_id = utils_obj.select_from_table(
                        table_name=EXPENSES_CATEGORY_TABLE,
                        column_name="expenses_category_id",
                        where_clause=f"expenses_sub_category = '{category}'",
                    )[0][0]
                    count_of_this_category = (
                        utils_obj.select_from_table(
                            table_name=EXPENSES_CATEGORY_TABLE,
                            column_name="count",
                            where_clause=f"expenses_sub_category = '{category}'",
                        )[0][0]
                        + 1
                    )
                    utils_obj.update_in_table(
                        table_name=EXPENSES_CATEGORY_TABLE,
                        column_name="count",
                        value=count_of_this_category,
                        where_clause=f"expenses_sub_category = '{category}'",
                    )
            user_id = utils_obj.select_from_table(
                table_name="login", column_name="login_id", where_clause=f"username = '{username}'"
            )[0][0]
            utils_obj.insert_into_table(
                table_name=EXPENSES_TABLE,
                column_names="bank_name, id, expenses_category_id, amount, date, description",
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
        return EXPENSES_ADDED_SUCCESSFULLY


if __name__ == "__main__":
    print(
        ExpensesController.insert_expenses_details(
            bank_name="HDFC",
            username="abhijitashok",
            category="Zoo",
            amount=300,
            date="2022-08-30",
            description="Arignar Anna",
        )
    )
