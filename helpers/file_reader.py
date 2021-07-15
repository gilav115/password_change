from __future__ import absolute_import
import json


class FileReader:
    def __init__(self):
        pass

    @staticmethod
    def read_json(full_path):
        with open(full_path, "r") as read_file:
            data = json.load(read_file)

        return data
