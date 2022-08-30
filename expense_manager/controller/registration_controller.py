from expense_manager.db.db_utils import DbUtils
from expense_manager.constants.exception_constants import (
    USERNAME_ALREADY_EXISTS_ERROR,
    PASSWORDS_DONT_MATCH_ERROR,
    REGISTRATION_SUCCESS,
)
from expense_manager.controller.login_controller import LoginController


class RegistrationController:
    def __init__(self):
        pass

    def is_password_match(self, password, confirm_password):
        if password != confirm_password:
            return False
        else:
            return True

    def registration(self, username, password, confirm_password, name, phone_number):
        if LoginController().is_username_exist(username):
            return USERNAME_ALREADY_EXISTS_ERROR
        elif not self.is_password_match(password, confirm_password):
            return PASSWORDS_DONT_MATCH_ERROR
        id = DbUtils().id_generator(table_name="user")
        DbUtils().insert_into_table(table_name="user", values=f"{id}, '{name}', '{phone_number}'")
        DbUtils().insert_into_table(table_name="login", values=f"'{username}','{password}'")
        return REGISTRATION_SUCCESS


if __name__ == "__main__":
    reg_control = RegistrationController()
    print(reg_control.registration(username="priyav",password="priyav123",confirm_password="priyav123", name="Priya Venkat",phone_number="7826776233"))
