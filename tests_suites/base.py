import pytest
from helpers.consts import PasswordType, ValidPasswords, InvalidPasswords
from helpers.exceptions import InvalidPasswordException


@pytest.fixture
def old_password():
    return ValidPasswords.old_pass


@pytest.fixture
def valid_passwords():
    return ValidPasswords


@pytest.fixture
def invalid_passwords():
    return InvalidPasswords
