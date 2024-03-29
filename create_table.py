from connect_db import Database

def create_table():
    users = """
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            full_name VARCHAR NOT NULL,
            card_number VARCHAR UNIQUE NOT NULL,
            balance NUMERIC NOT NULL,
            password VARCHAR NOT NULL,
            phone_number VARCHAR,
            expire_date TIMESTAMP DEFAULT now())"""

    sms = """
        CREATE TABLE sms(
            notification_id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(user_id),
            phone_number VARCHAR,
            message VARCHAR NOT NULL)"""

    data = {
        "users": users,
        "sms": sms,
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()