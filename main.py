
# Password Manager Main Script
import verification      # Handles master password verification
import getpass           # For secure password input
import os                # For file operations
import user_password_setup  # Add new passwords
import set_up_master_password  # Set up/change master password
import delete_master_password  # Delete master password
import view_passwords         # View all saved passwords


# Check if master password file exists or is empty; if so, prompt to set a new master password
if not os.path.exists("master.hash") or os.path.getsize("master.hash") == 0:
    new_master_password = getpass.getpass("Enter a new master password: ")
    set_up_master_password.master_password(m_password=new_master_password)
    print()


# Master password verification loop
while True:
    user_input = getpass.getpass("Please enter the master password: ")
    if verification.verification(user_input):
        print("Verification Success!")
        break
    else:
        print("Wrong password!")


# Main menu loop for password manager options
while True:
    print("---------Welcome to the Password Manager!---------")
    print("1. Add a new password")
    print("2. Check all the passwords")
    print("3. Set a new master password")
    print("4. Delete a password")
    print("5. Delete the master password")
    print("6. Exit")
    menu_input = input("Please select an option>> ")
    if menu_input == "1":
        user_password_setup.setup_user_password()
        print()
    elif menu_input == "2":
        view_passwords.view_passwords()
        print()
    elif menu_input == "3":
        new_master_password = getpass.getpass("Enter a new master password: ")
        set_up_master_password.master_password(m_password=new_master_password)
        print()
    elif menu_input == "4":
        import delete_password
        delete_password.delete_password()
        print()
    elif menu_input == "5":
        delete_master_password.delete_master_password()
        print()
    elif menu_input == "6":
        print("Exiting the Password Manager. Goodbye!")
        break
    else:
        print("Invalid option selected. Please try again.\n")




