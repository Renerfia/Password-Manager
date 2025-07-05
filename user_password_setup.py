
# Add a new password to the database
import sqlite3

def setup_user_password():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    # Ensure the table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT,
            user_name TEXT,
            email TEXT,
            password TEXT
        )
    """)
    conn.commit()
    # Prompt user for password details
    service = input("Enter the service name: ")
    user_name = input("Enter the user name: ")
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    cursor.execute("""
        INSERT INTO passwords (service, user_name, email, password)
        VALUES (?, ?, ?, ?)
    """, (service, user_name, email, password))
    conn.commit()
    conn.close()
    print("User password setup completed successfully!\n")

