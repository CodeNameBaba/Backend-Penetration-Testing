import main as baba
import json

with open("users.json", "r") as file:
    users = json.load(file)

x = baba.login(users)
baba.transfer(users, x)