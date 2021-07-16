class PasswordType:
    default = "default"
    strict = "strict"


class RequirementType:
    number = 'number'
    percentage = 'percentage'


class ValidPasswords:
    old_pass = "12345AaSsDdFfGgHh!@#*"
    new_pass = "67890QqqqqEeRr##**"
    similar_old_78 = "12345AasDffHhhhh!@#*"
    similar_old_79 = "12345AaSsDfHhhhhEe!@#*"
    one_upper_case = "67890Qqqqqeeer##**"
    one_lower_case = "67890QTYUIEeRr##**"
    one_numeric = "6gnfQqqqqggEeRr##**"
    one_special_char = "67890QqqqqEeRrVbb*"


class InvalidPasswords:
    too_short = "123AaSsDdh!@"
    illegal_chars = "67890QqWwEeRrTtYy##**^"
    similar_old_86 = "12345AaSsDdFfHhhhhh!@#*"
    similar_old_80 = "12345AaSsDfHhhhhE!@#*"
    no_upper_case = "67890qqwweerrttyy##**"
    no_lower_case = "67890QQWWEERRTTYY##**"
    no_numeric = "zxcvbQqWwEeRrTtYy##**"
    no_special_chars = "67890QqWwEeRrTtYyUuIi"
    too_many_special_chars = "67890QqWwEeRrTtYy##**@!"
    too_many_duplicates = "zzzzz67890QqEeRrTtYy##**"
    too_many_numeric = "679034343434344QqEeRrTtYy##**"
    empty = ''
