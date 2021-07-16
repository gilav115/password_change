from validators.password_validator import *


class StrictPasswordValidator(PasswordValidator):
    """
    Password requirement
    1. At least 18 alphanumeric characters and list of special chars !@#$&*
    2. At least 1 Upper case, 1 lower case ,least 1 numeric, 1 special character
    3. No duplicate repeat characters more than 4
    4. No more than 4 special characters
    5. 50 % of password should not be a number

    Change password requirement
    1. Old password should match with system
    2. New password should be a valid password
    3. password is not similar to old password < 80% match.
    """

    def __init__(self):
        super().__init__(pass_type=PasswordType.strict)

    def validate_new_password(self, password, old_password):
        if not password:
            raise InvalidPasswordException("You must provide a new password")

        if not old_password:
            raise InvalidPasswordException("In order to change password you must provide your old/current password")

        # At least 18 alphanumeric characters
        if not self.long_enough(password):
            value = self.conf['length']['min']['value']
            raise InvalidPasswordException(f"Password must be at least {value} chars length")

        # Before checking anything else, make sure only allowed chars are used
        if self.contains_illegal_chars(password):
            legal = self.conf['special']['legal']
            raise InvalidPasswordException(f"Only alphanumeric values and these chars {legal} are allowed")

        # password is not similar to old password < 80% match.
        if self.old_password_conflict(old_password, password):
            raise InvalidPasswordException("New password is too similar to an old password you already used")

        # At least 1 upper case
        if not self.satisfy_upper_case_requirements(password):
            value = self.conf['upper_case']['min']['value']
            raise InvalidPasswordException(f"Password must include at least {value} upper case letters")

        # At least 1 lower case
        if not self.satisfy_lower_case_requirements(password):
            value = self.conf['lower_case']['min']['value']
            raise InvalidPasswordException(f"Password must include at least {value} lower case letters")

        # At least 1 numeric. 50 % of password should not be a number.
        if not self.satisfy_numeric_requirements(password):
            min_value = self.conf['numeric']['min']['value']
            max_value = self.conf['numeric']['max']['value']
            error = f"Password must include at least {min_value} numeric value and less than {max_value}% of total password length"
            raise InvalidPasswordException(error)

        # At least one special char. No more than 4 special characters. List of special chars !@#$&*
        if not self.satisfy_special_char_requirements(password):
            min_value = self.conf['special']['min']['value']
            max_value = self.conf['special']['max']['value']
            legal = self.conf['special']['legal']
            error = f"Password must include {min_value}-{max_value} of these special chars {legal}"
            raise InvalidPasswordException(error)

        # No duplicate repeat characters more than 4
        if self.too_many_duplicates(password):
            value = self.conf['duplicates']['max']['value']
            raise InvalidPasswordException(f"Password can have up to {value} of duplicated chars")
