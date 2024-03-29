from connect_db import Database
import  login
import register

def main():
    service = input("""
    1. Login
    2. Register
    0. Stop
        >>> """)

    if service == '1':
        return login.login()

    elif service == '2':
       return register.register()

    elif service == '0':
        while service == '0':
            break

    else:
        print("Error")
        return main()


if __name__ == "__main__":
    main()