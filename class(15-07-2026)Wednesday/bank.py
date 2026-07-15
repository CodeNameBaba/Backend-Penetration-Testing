import main as asad
import json

with open("users.json", "r") as file:
    users = json.load(file)

x = asad.login(users)
asad.transfer(users, x)