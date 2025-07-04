import sqlite3
import getpass
import bcrypt
# Function to verify the master password

def verification(user_input):

    try:
        
        with open("master.hash","rb") as m:
            stored = m.read()
        return bcrypt.checkpw(user_input.encode(),stored)
    except FileNotFoundError:
        print("File not found! please create a master password")
        return False

