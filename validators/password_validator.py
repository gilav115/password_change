import re
from collections import Counter
from helpers.configuration_fetcher import ConfigurationFetcher
from helpers.consts import RequirementType, ValidPasswords, PasswordType
from difflib import SequenceMatcher
from helpers.exceptions import InvalidPasswordException


class PasswordValidator:
    def __init__(self, pass_type='default'):
        self.old_password = ValidPasswords.old_pass
        self.conf = ConfigurationFetcher.fetch(pass_type)

    def is_valid(self, password):
        raise NotImplementedError("Implement this function at your password validator")

    def is_old(self, password):
        """
        Mock for an old password, using hard coded password
        :param password: new password
        :return: True if new password match const old password
        """
        return password == self.old_password

    def long_enough(self, password):
        return self.satisfy_min_requirement(self.conf['length'], len(password))

    def short_enough(self, password):
        return self.satisfy_max_requirement(self.conf['length'], len(password))

    def old_password_conflict(self, old_password, password):
        conf = self.conf['old_password']
        if not conf['max']:
            return False

        return self.similarity(old_password, password) > conf['max']['value']

    def contains_illegal_chars(self, password):
        special = self.conf['special']['legal']
        reg = f"^[a-zA-Z0-9{special}]*$"
        res = re.search(reg, password)
        return res is None

    def satisfy_upper_case_requirements(self, password):
        upper_case = self.pattern_count("[A-Z]", password)
        min_req = self.satisfy_min_requirement(self.conf['upper_case'], upper_case)
        max_req = self.satisfy_max_requirement(self.conf['upper_case'], upper_case)
        return min_req and max_req

    def satisfy_lower_case_requirements(self, password):
        lower_case = self.pattern_count("[a-z]", password)
        min_req = self.satisfy_min_requirement(self.conf['lower_case'], lower_case)
        max_req = self.satisfy_max_requirement(self.conf['lower_case'], lower_case)
        return min_req and max_req

    def satisfy_numeric_requirements(self, password):
        numeric = self.pattern_count("[0-9]", password)
        min_req = self.satisfy_min_requirement(self.conf['numeric'], numeric)
        max_req = self.satisfy_max_requirement(self.conf['numeric'], numeric, len(password))
        return min_req and max_req

    def satisfy_special_char_requirements(self, password):
        special = self.pattern_count("[!@#$&*]", password)
        min_req = self.satisfy_min_requirement(self.conf['special'], special)
        max_req = self.satisfy_max_requirement(self.conf['special'], special)
        return min_req and max_req

    def too_many_duplicates(self, password):
        counter = Counter(password)
        max_dup = max(counter.values())
        return not self.satisfy_max_requirement(self.conf['duplicates'], max_dup)

    def pattern_count(self, pattern, password):
        res = re.findall(pattern, password)
        return len(res)

    def satisfy_min_requirement(self, conf, length, full_length=None):
        min_conf = conf['min']
        if not min_conf:
            return True

        req_type = min_conf['type']
        value = min_conf['value']

        if req_type == RequirementType.number:
            satisfy = length >= value
        elif req_type == RequirementType.percentage:
            satisfy = 100 * float(length) / float(full_length) >= value
        else:
            raise ValueError(f"Unsupported requirement type {req_type}")

        return satisfy

    def satisfy_max_requirement(self, conf, length, full_length=None):
        max_conf = conf['max']
        if not max_conf:
            return True

        req_type = max_conf['type']
        value = max_conf['value']

        if req_type == RequirementType.number:
            satisfy = length <= value
        elif req_type == RequirementType.percentage:
            satisfy = 100 * float(length) / float(full_length) <= value
        else:
            raise ValueError(f"Unsupported requirement type {req_type}")

        return satisfy

    def similarity(self, old_pass, new_pass):
        """
       Using built-in package that returns similarity rartio
        e.g.
        s = SequenceMatcher(None, "abcd", "bcde")
        s.ratio() ==> 0.75
        :param old_pass:
        :param new_pass:
        :return: similarity in percentage 0 - 100, always as an int (70 and not 70.01)
        """
        s = SequenceMatcher(None, old_pass, new_pass)
        return int(s.ratio() * 100)

    def include(self, pattern, s):
        res = re.search(pattern, s)
        return res is not None
