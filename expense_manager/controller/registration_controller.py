from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.exception_constants import (
    USERNAME_ALREADY_EXISTS_ERROR,
    PASSWORDS_DONT_MATCH_ERROR,
)
from expense_manager.constants.success_constants import REGISTRATION_SUCCESS
from expense_manager.controller.login_controller import LoginController
from expense_manager.constants.table_names import LOGIN_TABLE, USER_TABLE


class RegistrationController:
    def __init__(self):
        pass

    @staticmethod
    def insert_registration_record(username, password, confirm_password, name, phone_number):
        if LoginController().is_username_exist(username):
            return USERNAME_ALREADY_EXISTS_ERROR
        elif not DbUtils.is_value_match(value1=password, value2=confirm_password):
            return PASSWORDS_DONT_MATCH_ERROR
        with DbUtils() as utils_obj:
            utils_obj.insert_into_table(
                table_name=USER_TABLE,
                column_names="name, phone_number",
                values=f"'{name}','{phone_number}'",
            )
            utils_obj.insert_into_table(
                table_name=LOGIN_TABLE,
                column_names="username,password",
                values=f"'{username}','{password}'",
            )
        return REGISTRATION_SUCCESS


if __name__ == "__main__":
    print(
        RegistrationController.insert_registration_record(
            username="priyav",
            password="priyav123",
            confirm_password="priyav123",
            name="Priya Venkat",
            phone_number="7826776233",
        )
    )
