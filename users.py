from connect_db import Database
import main


def data(phone_number):
    query = "SELECT * FROM users"
    data = Database.connect(query, "select")

    for i in data:
        print(f"""
        ID: {i[0]}
        Full_name: {i[1]}
        Card_number: {i[2]}
        Balance: {i[3]}
        Password: {i[4]}
        Phone_number: {i[5]}
        Expire_date: {i[6]}""")

    return users(phone_number)


def get_cash(phone_number):
    query = "SELECT balance FROM users"
    data = Database.connect(query, "select")
    for i in data:
        a = i[0]
        print(a)
        money = int(input("Enter money: "))
        if money <= i[0]:
            x = i[0] - money
            x = i[0]
            query = f"UPDATE users SET balance = {x} WHERE balance = {a}"
            dataa = Database.connect(query, "update")
            print("Sucssesful")
            return users(phone_number)
    print("Funds are insufficient")
    return get_cash(phone_number)

def balance(phone_number):
    query = "SELECT balance FROM users"
    dataa = Database.connect(query, "select")
    for i in dataa:
        print(f"""
        \nBalance: {i[0]}\n""")
        return users(phone_number)



def sms(phone_number):
    check = input("""
    1. Connect SMS notification
    2. Delete SMS notification
    0. Logaut
          >>> """)

    if check == "1":
        query = "SELECT phone_number FROM users"
        dataa = Database.connect(query, "select")
        for i in dataa:
            user = input("User id: ")
            phone = input("Enter your phone number: ")
            while i[0] == "":
                query = f"UPDATE users SET phone_number = '{phone}' WHERE phone_number = ''"
                dataa = Database.connect(query, "update")
                print("Updated")
                return sms(phone_number)

        print("Karta allaqachon nomer ulangan")
        return sms(phone_number)

    elif check == "2":
        cek = input("""
        1. Delete
        0. Logaut
              >>> """)

        if cek == "1":
            query = "SELECT phone_number FROM users"
            dataa = Database.connect(query, "select")
            for i in dataa:
                phone = input("Enter phone number: ")
                if phone == i[0]:
                    query = f"UPDATE users SET phone_number = '' WHERE phone_number = '{phone}'"
                    dataa = Database.connect(query, "delete")
                    print("Successful")
                return sms(phone_number)


        elif cek == "0":
            return sms(phone_number)

        else:
            print("Error")
            return sms(phone_number)

    elif check == "0":
        return users(phone_number)



def users(phone_number):
    user = input("""
    
    1. Data
    2. Connect SMS notification
    3. Balance
    4. Get cash
    0. Logaut
           >>> """)

    if user == "1":
        return data(phone_number)

    elif user == "2":
        return sms(phone_number)

    elif user == "3":
        return balance(phone_number)

    elif user == "4":
        return get_cash(phone_number)

    elif user == "0":
        return main.main()

    else:
        print("\nError\n")
        return users(phone_number)