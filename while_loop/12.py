username = "admin"
password = "password"
i = 0
while i < 1:
    a = input("Enter the username:")
    b = input("Enter the password:")
    if a == username and b == password:
        print("logged in successfully")
    else:
        print("Invalid user")
    i = i + 1
