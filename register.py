from connect_db import Database
import login


def register():
    print("Register Page")
    full_name = input("Full Name: ")
    card_number = input("Card Number: ")
    while len(card_number) != 16:
        print("\nBunday yoza olmaysiz\n")
        card_number = input("Card Number: ")
    balance = input("Balance: ")
    password = input("Password: ")
    phone_number = input("Phone Number: ")

    query = f"""INSERT INTO users(full_name, card_number, balance, password, phone_number) 
    VALUES('{full_name}', '{card_number}', {balance}, '{password}', '{phone_number}')"""

    print(Database.connect(query, "insert"))
    return login.login()