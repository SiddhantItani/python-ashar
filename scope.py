is_Login=False
def login(username, password):
    if username=="admin" and password=="admin":
        global is_Login
        is_Login= True

login("admin", "admin")
print(is_Login)
