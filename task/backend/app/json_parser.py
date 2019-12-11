import json
import os
from pprint import pprint


class JsonParser:
    def __init__(self):
        self.foo = {}

        CURRENT_DIRECTORY = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        DATA_FILE = os.path.join(CURRENT_DIRECTORY, "data.json")

        with open(DATA_FILE, "r") as data_file:
            data = data_file.read()
        self.foo = json.loads(data)

    def user_usage(self):
        return self.foo.get("data")

    def domainX(self):
        return self.foo.get("domainX")

    def domainY(self):
        return self.foo.get("domainY")

    def categoriesY(self):
        return self.foo.get("categoriesY")
