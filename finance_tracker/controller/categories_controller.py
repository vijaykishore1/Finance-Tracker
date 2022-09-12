from finance_tracker.db.db_utils import DbUtils
from finance_tracker.constants.table_names import (
    EXPENSES_CATEGORY_TABLE,
    INVESTMENTS_CATEGORY_TABLE,
    INCOME_CATEGORY_TABLE,
)
from finance_tracker.constants.exception_constants import (
    CATEGORY_ALREADY_EXISTS_ERROR,
    SUB_CATEGORY_ALREADY_EXISTS_ERROR,
)
from finance_tracker.constants.success_constants import CATEGORY_ADDED_SUCCESSFULLY


class ExpensesCategoriesController:
    def __init__(self):
        pass

    @staticmethod
    def is_category_exists(category):
        with DbUtils() as utils_obj:
            category_list = utils_obj.select_from_table(
                column_name="expenses_category",
                table_name=EXPENSES_CATEGORY_TABLE,
                where_clause=f"expenses_category = '{category}'",
            )
        if category_list:
            return True
        else:
            return False

    @staticmethod
    def is_sub_category_exists(sub_category):
        with DbUtils() as utils_obj:
            sub_category_list = utils_obj.select_from_table(
                column_name="expenses_sub_category",
                table_name=EXPENSES_CATEGORY_TABLE,
                where_clause=f"expenses_sub_category = '{sub_category}'",
            )
        if sub_category_list:
            return True
        else:
            return False

    @staticmethod
    def insert_category_details(category, sub_category):
        # if ExpensesCategoriesController.is_category_exists(category):
        #     return CATEGORY_ALREADY_EXISTS_ERROR
        # elif ExpensesCategoriesController.is_sub_category_exists(sub_category):
        #     return SUB_CATEGORY_ALREADY_EXISTS_ERROR
        with DbUtils() as utils_obj:
            utils_obj.insert_into_table(
                table_name=EXPENSES_CATEGORY_TABLE,
                column_names="expenses_category, expenses_sub_category",
                values=f"'{category}','{sub_category}'",
            )
        return CATEGORY_ADDED_SUCCESSFULLY


class InvestmentsCategoriesController:
    def __init__(self):
        pass

    @staticmethod
    def is_category_exists(category):
        with DbUtils() as utils_obj:
            category_list = utils_obj.select_from_table(
                column_name="investments_category",
                table_name=INVESTMENTS_CATEGORY_TABLE,
                where_clause=f"investments_category = '{category}'",
            )
        if category_list:
            return True
        else:
            return False

    @staticmethod
    def is_sub_category_exists(sub_category):
        with DbUtils() as utils_obj:
            sub_category_list = utils_obj.select_from_table(
                column_name="investments_sub_category",
                table_name=INVESTMENTS_CATEGORY_TABLE,
                where_clause=f"investments_sub_category = '{sub_category}'",
            )
        if sub_category_list:
            return True
        else:
            return False

    @staticmethod
    def insert_category_details(category, sub_category):
        if InvestmentsCategoriesController.is_category_exists(category):
            return CATEGORY_ALREADY_EXISTS_ERROR
        elif InvestmentsCategoriesController.is_sub_category_exists(sub_category):
            return SUB_CATEGORY_ALREADY_EXISTS_ERROR
        with DbUtils() as utils_obj:
            utils_obj.insert_into_table(
                table_name=INVESTMENTS_CATEGORY_TABLE,
                column_names="investments_category, investments_sub_category",
                values=f"'{category}','{sub_category}'",
            )
        return CATEGORY_ADDED_SUCCESSFULLY


class IncomeCategoriesController:
    def __init__(self):
        pass

    @staticmethod
    def is_category_exists(category):
        with DbUtils() as utils_obj:
            category_list = utils_obj.select_from_table(
                column_name="income_category",
                table_name=INCOME_CATEGORY_TABLE,
                where_clause=f"income_category = '{category}'",
            )
        if category_list:
            return True
        else:
            return False

    @staticmethod
    def is_sub_category_exists(sub_category):
        with DbUtils() as utils_obj:
            sub_category_list = utils_obj.select_from_table(
                column_name="income_sub_category",
                table_name=INCOME_CATEGORY_TABLE,
                where_clause=f"income_sub_category = '{sub_category}'",
            )
        if sub_category_list:
            return True
        else:
            return False

    @staticmethod
    def insert_category_details(category, sub_category):
        if IncomeCategoriesController.is_category_exists(category):
            return CATEGORY_ALREADY_EXISTS_ERROR
        elif IncomeCategoriesController.is_sub_category_exists(sub_category):
            return SUB_CATEGORY_ALREADY_EXISTS_ERROR
        with DbUtils() as utils_obj:
            utils_obj.insert_into_table(
                table_name=INCOME_CATEGORY_TABLE,
                column_names="income_category, income_sub_category",
                values=f"'{category}','{sub_category}'",
            )
        return CATEGORY_ADDED_SUCCESSFULLY


# if __name__ == '__main__':
# print(ExpensesCategoriesController.insert_category_details(category="Leisure", sub_category="Movie"))
