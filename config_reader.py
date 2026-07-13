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
    @property
    def alert_url(self):
        return self.data["alert_url"]
    @property
    def context_menu_url(self):
        return self.data["context_menu_url"]


a = ConfigReader()
print(a.main_url, a.login, a.password)
