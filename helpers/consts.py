class PasswordType:
    default = "default"
    strict = "strict"


class RequirementType:
    number = 'number'
    percentage = 'percentage'


class Passwords:
    valid = {
        "old": "12345AaSsDdFfGgHh!@#*",
    }

    invalid = {
        "too_short": "123AaSsDdh!@",
        "no_upper": "12345aassddffgghh!@#*",
        "no_lower": "12345AASSDDFFGGHH!@#*",
        "no_numeric": "QqWwEeAaSsDdFfGgHh!@#*",
        "no_special": "12345AaSsDdFfGgHhQqWwEe",
    }
