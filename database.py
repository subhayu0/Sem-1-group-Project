import sqlite3
from datetime import datetime
db_name="pursepal.db"
conn = sqlite3.connect(db_name)
create_tables()

def create_tables():
        with conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS User (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL,
                email_address VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL
            );
            ''')

            conn.execute('''
            CREATE TABLE IF NOT EXISTS Wallet (
                wallet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                balance INTEGER NOT NULL DEFAULT 0,
                user_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES User(user_id)
            );
            ''')

            conn.execute('''
            CREATE TABLE IF NOT EXISTS Transaction (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                transaction_date VARCHAR(255) NOT NULL,
                transaction_amount FLOAT NOT NULL,
                wallet_id INTEGER NOT NULL,
                FOREIGN KEY(wallet_id) REFERENCES Wallet(wallet_id)
            );
            ''')

def add_user( name, email_address, password):
        with conn:
            conn.execute('''
            INSERT INTO User (name, email_address, password)
            VALUES (?, ?, ?);
            ''', (name, email_address, password))

def add_wallet( user_id, initial_balance=0):
        with conn:
            conn.execute('''
            INSERT INTO Wallet (balance, user_id)
            VALUES (?, ?);
            ''', (initial_balance, user_id))

def add_transaction( wallet_id, transaction_amount):
        with conn:
            transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            conn.execute('''
            INSERT INTO Transaction (transaction_date, transaction_amount, wallet_id)
            VALUES (?, ?, ?);
            ''', (transaction_date, transaction_amount, wallet_id))
            update_wallet_balance(wallet_id, transaction_amount)

def update_wallet_balance( wallet_id, transaction_amount):
        with conn:
            conn.execute('''
            UPDATE Wallet
            SET balance = balance + ?
            WHERE wallet_id = ?;
            ''', (transaction_amount, wallet_id))

def get_user( user_id):
        with conn:
            return conn.execute('''
            SELECT * FROM User WHERE user_id = ?;
            ''', (user_id,)).fetchone()

def get_wallet( user_id):
        with conn:
            return conn.execute('''
            SELECT * FROM Wallet WHERE user_id = ?;
            ''', (user_id,)).fetchall()

def get_transactions( wallet_id):
        with conn:
            return conn.execute('''
            SELECT * FROM Transaction WHERE wallet_id = ?;
            ''', (wallet_id,)).fetchall()

def close():
        conn.close()