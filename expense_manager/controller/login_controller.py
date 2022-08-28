from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.table_names import LOGIN_TABLE


class LoginController:
    def __init__(self):
        pass

    def is_username_exist(self, username):
        obj = DbUtils()
        user_list = obj.select_from_table(column_name="username", table_name=LOGIN_TABLE,
                                          where_clause=f"where username = '{username}'")
        if user_list:
            return True
        else:
            # TODO
            return False

    def validate_login(self, username, password):
        if not self.is_username_exist:
            return "username does not exist"  # create a variable later in exception.py in constants called USERNAME_DOES_NOT_EXIST_ERROR


if __name__ == '__main__':
    loginobject = LoginController()
    print(loginobject.validate_login(username="vijay", password="Vijay123"))
