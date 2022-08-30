from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.table_names import LOGIN_TABLE
from expense_manager.constants.exception_constants import PASSWORD_NOT_VALIDATED, \
    USERNAME_DOES_NOT_EXIST_ERROR
from expense_manager.constants.success_constants import PASSWORD_VALIDATED


class LoginController:
    def __init__(self):
        pass

    def is_username_exist(self, username):
        obj = DbUtils()
        user_list = obj.select_from_table(column_name="username", table_name=LOGIN_TABLE,
                                          where_clause=f"username = '{username}'")
        if user_list:
            return True
        else:
            return False

    def validate_login(self, username, password):
        obj = DbUtils()
        if not self.is_username_exist(username):
            return USERNAME_DOES_NOT_EXIST_ERROR
        pwd_to_check = obj.select_from_table(column_name="password", table_name=LOGIN_TABLE,
                                             where_clause=f"username = '{username}'")
        assert len(pwd_to_check[0]) == 1
        if password == pwd_to_check[0][0]:
            return PASSWORD_VALIDATED
        else:
            return PASSWORD_NOT_VALIDATED


if __name__ == '__main__':
    login_object = LoginController()
    print(login_object.validate_login(username="priyav", password="priyav123"))
    # utils_obj = DbUtils()
    # utils_obj.select_from_table(table_name="login")
