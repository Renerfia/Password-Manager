import sqlite3




def setup_user_password():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    # Drop the table if it exists to fix column name issues (run once, then remove these two lines)
    cursor.execute("DROP TABLE IF EXISTS passwords")
    conn.commit()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT,service,user_name,email,password)
""")
    conn.commit()
    service = input("Enter the service name: ")
    user_name = input("Enter the user name: ")
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    cursor.execute("""
        INSERT INTO passwords (service, user_name, email, password)
        VALUES (?, ?, ?, ?)
    """, (service, user_name, email, password))
    conn.commit()
    print("User password setup completed successfully!")

