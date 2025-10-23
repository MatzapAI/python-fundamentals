print("---LOGIN SYSTEM---")

attempts = 3

while attempts > 0:
    user = input("Enter a user: ")
    password = input("Enter a password: ")
    
    if user == "admin" and password == "admin123":
        print(f"Welcome {user}")
        break
    else:
        attempts -= 1
        print(f"Incorrect user or password, left attemps: {attempts}")
if attempts == 0:       
    print("Too many failed attempts. Closing the program...")        