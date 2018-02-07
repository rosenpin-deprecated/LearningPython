import json

'''
ATM like program
Allow users to log in and perform actions related to their accounts
Pull money
Deposit money
Check status of their savings
Change password
'''


class User:
    def __init__(self, id, passwd, money):
        self.passwd = passwd
        self.money = int(money)
        self.id = id

    def __str__(self):
        return "id:%s money: %s, passwd: %s" % (self.id, self.money, self.passwd)


def menu(user_to_modify):
    print("1. Check moneyz \t 2. Pull moneyz \n 3. Put moneyz \t 4. Change password \n -1. Exit")
    task = int(input(">>> Enter your selection"))
    if task == 1:
        print(user_to_modify.money)
    elif task == 2:
        amount = input("How much do you want to pull?")
        user_to_modify.money -= int(amount)
    elif task == 3:
        amount = input("How much do you want to put?")
        user_to_modify.money += int(amount)
    elif task == 4:
        newpass = input("Enter new password")
        user_to_modify.passwd = newpass
    elif task == -1:
        for u in parsed_users:
            u["money"] = users[u["id"]].money
            u["passwd"] = users[u["id"]].passwd
        with open("users.json", 'w') as usersfile:
            usersfile.write(json.dumps(parsed_users))
        print("Goodbye :)")
        exit(0)
    else:
        print("Command not found")
    menu(user_to_modify)


with open("users.json", "r") as file:
    parsed_users = json.loads(file.read())
users = {}
for user in parsed_users:
    users[user["id"]] = (User(user["id"], user["passwd"], user["money"]))

uid = input(">>> Enter username")
if uid not in users:
    print("User not found!")
    exit(1)
password = input(">>> Enter password")
if password == users[uid].passwd:
    print("Access granted, you have")
    menu(users[uid])
else:
    print("Access denied, wrong password")
