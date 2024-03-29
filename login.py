from connect_db import Database
import users
from main import main

def login_2(phone_number):
    card_number = input("Card Number: ")
    while len(card_number) != 16:
        print("Bunday yoza olmaysiz")
        card_number = input("Card Number: ")
    password = input("Password: ")

    query = "SELECT * FROM users"
    data = Database.connect(query, "select")
    for i in data:
        if card_number == i[2] and password == i[4]:
            return users.users(phone_number)

    return main()

def login():
    print("\n<<<<<<<<<<<Login>>>>>>>>>>>>\n")

    query = "SELECT * FROM users"
    return login_2(query)