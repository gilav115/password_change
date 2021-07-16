from validators.password_validator import PasswordValidator
from validators.strict_password_validator import StrictPasswordValidator
from helpers.consts import PasswordType


class ValidatorsFactory:
    def __init__(self):
        pass

    @classmethod
    def create(cls, pass_type):
        if pass_type == PasswordType.default:
            validator = PasswordValidator()
        elif pass_type == PasswordType.strict:
            validator = StrictPasswordValidator()
        else:
            raise ValueError(f"Invalid password type {pass_type}")

        return validator
