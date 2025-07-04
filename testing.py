import bcrypt

#for password
password = b"linexgoodboy"
password1 = b"jhgbhdgahbd"
hashed = bcrypt.hashpw(password,bcrypt.gensalt())   

if bcrypt.checkpw(password1,hashed):
    print("It matches!")
else:
    print("Wrong password!")
