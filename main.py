import verification      # Handles master password verification
import getpass           # For secure password input
import os                # For file operations

# Check if master password file exists or is empty; if so, prompt to set a new master password
if not os.path.exists("master.hash") or os.path.getsize("master.hash") == 0:
    import set_up_master_password
    new_master_password = getpass.getpass("Enter a new master password:")
    set_up_master_password.master_password(m_password=new_master_password)
    print("\n")

# Master password verification loop
while True:
    user_input = getpass.getpass("Please enter the master password:")
    if verification.verification(user_input):
        print("Verification Success!")
        break   # Exit loop if password is correct
    else:
        print("Wrong password!")

# Main menu loop for password manager options
while True:
    print("---------Welcome to the Password Manager!---------")
    print("---------1. Add a new password---------")
    print("---------2. Check all the passwords---------")
    print("---------3. Set a new master password---------")
    print("---------4. Delete the master password---------")
    print("---------5. Exit---------")
    menu_input = input("Please select an option>> ")
    if menu_input == "1":
        import user_password_setup
        user_password_setup.setup_user_password()   # Add a new password
        print("\n")
    elif menu_input == "2":
        import view_passwords
        view_passwords.view_passwords()             # View all saved passwords
        print("\n")
    elif menu_input == "3":
        import set_up_master_password
        new_master_password = getpass.getpass("Enter a new master password:")
        set_up_master_password.master_password(m_password=new_master_password)  # Set a new master password
        print("\n")
    elif menu_input == "4":
        import delete_master_password
        delete_master_password.delete_master_password()   # Delete/clear the master password
        print("\n")
    elif menu_input == "5":
        print("Exiting the Password Manager. Goodbye!")
        break   # Exit the main menu loop
    else:
        print("Invalid option selected. Please try again.")
        print("\n")




