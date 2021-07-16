from validators.validators_factory import ValidatorsFactory
from helpers.exceptions import InvalidPasswordException


class PasswordManagers:
    def __init__(self, pass_type):
        self.validator = ValidatorsFactory.create(pass_type)

    def change_password(self, old_pass, new_pass):
        try:
            self.validator.validate_new_password(password=new_pass, old_password=old_pass)
        except InvalidPasswordException as e:
            print(f"Unable to change password: {e}")
            return False

        self.update_password(old_pass, new_pass)

        return True

    def update_password(self, old_pass, new_pass):
        pass

