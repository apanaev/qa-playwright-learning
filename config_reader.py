import json


class ConfigReader:
    def __init__(self):
        with open("config.json") as file:
            self.data = json.load(file)

    @property
    def main_url(self):
        return self.data["main_url"]

    @property
    def login(self):
        return self.data["login"]

    @property
    def password(self):
        return self.data["password"]


a = ConfigReader()
print(a.main_url, a.login, a.password)
