from tests_suites.base import *
from validators.validators_factory import ValidatorsFactory

# Fixtures


@pytest.fixture
def validator():
    return ValidatorsFactory.create(PasswordType.strict)


# Positive flow test Cases


def test_valid_password(validator, old_password, valid_passwords):
    validator.validate_new_password(valid_passwords.new_pass, old_password)


def test_one_upper_case_password(validator, old_password, valid_passwords):
    validator.validate_new_password(valid_passwords.one_upper_case, old_password)


def test_one_lower_case_password(validator, old_password, valid_passwords):
    validator.validate_new_password(valid_passwords.one_lower_case, old_password)


def test_one_numeric_password(validator, old_password, valid_passwords):
    validator.validate_new_password(valid_passwords.one_numeric, old_password)


def test_one_special_char_password(validator, old_password, valid_passwords):
    validator.validate_new_password(valid_passwords.one_special_char, old_password)


def test_not_too_similar_old_password(validator, old_password, valid_passwords):
    validator.validate_new_password(valid_passwords.similar_old_78, old_password)


def test_not_too_similar_old_password_border_case(validator, old_password, valid_passwords):
    validator.validate_new_password(valid_passwords.similar_old_79, old_password)

# Negative flow test Cases


def test_too_short_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"Password must be at least .*"):
        validator.validate_new_password(invalid_passwords.too_short, old_password)


def test_illegal_chars_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"Only alphanumeric values and these chars .*"):
        validator.validate_new_password(invalid_passwords.illegal_chars, old_password)


def test_identical_old_password(validator, old_password):
    with pytest.raises(InvalidPasswordException, match=r"New password is too similar to an old password .*"):
        validator.validate_new_password(old_password, old_password)


def test_too_similar_old_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"New password is too similar to an old password .*"):
        validator.validate_new_password(invalid_passwords.similar_old_86, old_password)


def test_too_similar_old_password_border_case(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"New password is too similar to an old password .*"):
        validator.validate_new_password(invalid_passwords.similar_old_80, old_password)


def test_no_upper_case_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"Password must include at least .* upper case letters"):
        validator.validate_new_password(invalid_passwords.no_upper_case, old_password)


def test_no_lower_case_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"Password must include at least .* lower case letters"):
        validator.validate_new_password(invalid_passwords.no_lower_case, old_password)


def test_no_numeric_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r".* numeric value and less than .*"):
        validator.validate_new_password(invalid_passwords.no_numeric, old_password)


def test_too_many_numeric_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r".* numeric value and less than .*"):
        validator.validate_new_password(invalid_passwords.too_many_numeric, old_password)


def test_no_special_chars_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"Password must include .* of these special chars"):
        validator.validate_new_password(invalid_passwords.no_special_chars, old_password)


def test_too_many_special_chars_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"Password must include .* of these special chars"):
        validator.validate_new_password(invalid_passwords.too_many_special_chars, old_password)


def test_too_many_duplicates_chars_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"Password can have up to .* of duplicated chars"):
        validator.validate_new_password(invalid_passwords.too_many_duplicates, old_password)


def test_empty_password(validator, old_password, invalid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"You must provide a new password"):
        validator.validate_new_password(invalid_passwords.empty, old_password)


def test_empty_password(validator, invalid_passwords, valid_passwords):
    with pytest.raises(InvalidPasswordException, match=r"In order to change password you must provide your old/current password"):
        validator.validate_new_password(valid_passwords.new_pass, invalid_passwords.empty)
