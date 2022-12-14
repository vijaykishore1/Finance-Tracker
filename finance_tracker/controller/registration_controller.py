from finance_tracker.db.db_utils import DbUtils
from finance_tracker.constants.exception_constants import (
    USERNAME_ALREADY_EXISTS_ERROR,
    PASSWORDS_DONT_MATCH_ERROR,
)
from finance_tracker.constants.success_constants import REGISTRATION_SUCCESS
from finance_tracker.controller.login_controller import LoginController
from finance_tracker.constants.table_names import LOGIN_TABLE, USER_TABLE


class RegistrationController:
    def __init__(self):
        pass

    @staticmethod
    def insert_registration_record(username, password, email):
        if LoginController().is_username_exist(username):
            return USERNAME_ALREADY_EXISTS_ERROR
        # elif not DbUtils.is_value_match(value1=password, value2=confirm_password):
        #     return PASSWORDS_DONT_MATCH_ERROR
        with DbUtils() as utils_obj:
            # utils_obj.insert_into_table(
            #     table_name=USER_TABLE,
            #     column_names="name, phone_number",
            #     values=f"'{name}','{phone_number}'",
            # )
            utils_obj.insert_into_table(
                table_name=LOGIN_TABLE,
                column_names="username,password,email",
                values=f"'{username}','{password}','{email}'",
            )
        return


if __name__ == "__main__":
    print(
        RegistrationController.insert_registration_record(
            username="priyav",
            password="priyav123",
            email="priyav@gmail.com"
        )
    )
