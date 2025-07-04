# Password Manager

A simple and secure command-line password manager for Windows.

---

## Features

- 🔒 **Master Password Protection:** All your passwords are secured with a master password (hashed for safety).
- 📝 **Add New Passwords:** Save service credentials (service name, username, email, password) to a local SQLite database.
- 👀 **View Passwords:** Display all saved passwords in the terminal.
- 🔄 **Change Master Password:** Set a new master password at any time.
- ❌ **Delete Master Password:** Clear the master password (forces setup on next run).
- 🖥️ **Simple CLI Menu:** Easy-to-use text-based interface.

---

## How to Use

1. **Download and run [`main.exe`](#)** (after building with PyInstaller, or run `main.py` with Python).
2. Follow the on-screen instructions to set up your master password and manage your passwords.

---

## Notes

- Your passwords are stored in `passwords.db` (SQLite database).
- The master password hash is stored in `master.hash`.
- **Do not share `passwords.db` or `master.hash` with anyone.**
- If you want to reset everything, just delete these two files.

---

## License

MIT License

