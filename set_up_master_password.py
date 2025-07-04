import sqlite3
import bcrypt
import getpass

#making master password in hash
def master_password(m_password):
    hashed = bcrypt.hashpw(m_password.encode(),bcrypt.gensalt())
    with open("master.hash","wb") as m:
        m.write(hashed)

    print("A new master password has been created!")

