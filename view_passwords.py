import sqlite3

def view_passwords():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM passwords")
    rows = cursor.fetchall()

    if not rows:
        print("No passwords found.")
    else:
        for row in rows:
            print(f"Service: {row[1]}, User Name: {row[2]}, Email: {row[3]}, Password: {row[4]}")

    conn.close()