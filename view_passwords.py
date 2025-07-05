import sqlite3

def view_passwords():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    # Ensure the table exists
   
    
    cursor.execute("SELECT service, user_name, email, password FROM passwords")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Service: {row[1]}, User Name: {row[2]}, Email: {row[3]}, Password: {row[4]}")
    else:
        print("No passwords found.")
    conn.close()