import main as m
import json

with open("users.json", "r") as file:
    users = json.load(file)

x = m.login(users)
m.transfer(users, x)