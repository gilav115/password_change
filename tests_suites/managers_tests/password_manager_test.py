from tests_suites.base import *
from managers.password_managers import PasswordManagers

# Fixtures


class ValidPasswordParams(object):
    def __init__(self):
        self.manager = PasswordManagers(PasswordType.strict)
        self.instances = [(self.manager, ValidPasswords.old_pass, ValidPasswords.new_pass),
                          (self.manager, ValidPasswords.old_pass, ValidPasswords.similar_old_78),
                          (self.manager, ValidPasswords.old_pass, ValidPasswords.similar_old_79),
                          (self.manager, ValidPasswords.old_pass, ValidPasswords.one_upper_case),
                          (self.manager, ValidPasswords.old_pass, ValidPasswords.one_lower_case),
                          (self.manager, ValidPasswords.old_pass, ValidPasswords.one_numeric),
                          (self.manager, ValidPasswords.old_pass, ValidPasswords.one_special_char)]


class InvalidPasswordParams(object):
    def __init__(self):
        self.manager = PasswordManagers(PasswordType.strict)
        self.instances = [(self.manager, ValidPasswords.old_pass, InvalidPasswords.too_short),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.illegal_chars),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.similar_old_86),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.similar_old_80),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.no_upper_case),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.no_lower_case),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.no_numeric),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.no_special_chars),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.too_many_special_chars),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.too_many_duplicates),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.too_many_numeric),
                          (self.manager, ValidPasswords.old_pass, InvalidPasswords.empty)]

# Test Cases


@pytest.mark.parametrize("manager, old_password, valid_password", ValidPasswordParams().instances)
def test_change_valid_password_success(manager, old_password, valid_password):
    assert manager.change_password(old_password, valid_password)


@pytest.mark.parametrize("manager, old_password, invalid_password", InvalidPasswordParams().instances)
def test_change_invalid_password_fail(manager, old_password, invalid_password):
    assert not manager.change_password(old_password, invalid_password)
