from __future__ import absolute_import
from helpers.file_reader import FileReader
from helpers.consts import PasswordType


class ConfigurationFetcher:
    def __init__(self):
        pass

    @staticmethod
    def fetch(pass_type):
        if pass_type == PasswordType.default:
            conf = FileReader.read_json("configurations/password_configuration.json")
        elif pass_type == PasswordType.strict:
            conf = FileReader.read_json("configurations/strict_password_configuration.json")
        else:
            raise ValueError(f"Invalid password type {pass_type}")

        return conf
