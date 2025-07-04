import os



def delete_master_password():
    file_path = "master.hash"
    if os.path.exists(file_path):
        # Open the file in write mode to clear its contents
        with open(file_path, "w") as f:
            pass  # This empties the file
        print("The master password has been cleared (file is now empty)")
    else:
        print("There is no master password file to clear")
