import sqlite3

def view_passwords():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    # Ensure the table exists
   
    
    cursor.execute("SELECT service, user_name, email, password FROM passwords")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"Service: {row[0]}, User Name: {row[1]}, Email: {row[2]}, Password: {row[3]}")
    else:
        print("No passwords found.")
    conn.close()