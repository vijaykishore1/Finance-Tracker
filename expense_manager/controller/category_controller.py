from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.table_names import CATEGORY_TABLE
from expense_manager.constants.exception_constants import CATEGORY_ALREADY_EXISTS_ERROR,SUB_CATEGORY_ALREADY_EXISTS_ERROR
from expense_manager.constants.success_constants import CATEGORY_ADDED_SUCCESSFULLY

class CategoriesController:
    def __init__(self):
        pass
    def is_category_exists(self,category,sub_category):
        category_list = DbUtils().select_from_table(column_name="category", table_name=CATEGORY_TABLE,
                                          where_clause=f"category = '{category}'")
        if category_list:
            if self.is_sub_category_exists(sub_category):
                return True
            else:
                return False
        else:
            return False

    def is_sub_category_exists(self, sub_category):
        category_list = DbUtils().select_from_table(column_name="sub_category", table_name=CATEGORY_TABLE,
                                                    where_clause=f"sub_category = '{sub_category}'")
        if category_list:
            return True
        else:
            return False

    def category_details(self,category, sub_category):
        if self.is_category_exists(category,sub_category):
            return CATEGORY_ALREADY_EXISTS_ERROR
        elif self.is_sub_category_exists(sub_category):
            return SUB_CATEGORY_ALREADY_EXISTS_ERROR
        DbUtils().insert_into_table(table_name=CATEGORY_TABLE, column_names="category, sub_category",
                                    values=f"'{category}','{sub_category}'")
        return CATEGORY_ADDED_SUCCESSFULLY

if __name__ == '__main__':
    categories_control = CategoriesController()
    print(categories_control.category_details(category="Leisure", sub_category="Movie"))