"""
delete_password.py
Allows the user to delete a password entry from the database by selecting from a list.
"""

import sqlite3

DB_FILE = "passwords.db"

def delete_password():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, service, user_name, email FROM passwords")
    rows = cursor.fetchall()
    if not rows:
        print("No passwords to delete.")
        conn.close()
        return
    print("\nSaved Passwords:")
    for row in rows:
        print(f"ID: {row[0]}, Service: {row[1]}, User Name: {row[2]}, Email: {row[3]}")
    try:
        del_id = int(input("Enter the ID of the password to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid ID number.")
        conn.close()
        return
    cursor.execute("DELETE FROM passwords WHERE id = ?", (del_id,))
    if cursor.rowcount == 0:
        print("No password found with that ID.")
    else:
        conn.commit()
        print("Password deleted successfully.")
    conn.close()
