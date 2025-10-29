

print("---MENU SYSTEM---")

while True:
    print("=== Menú Principal ===")
    print("1. Greet")
    print("2. Calculate the square of a number")
    print("3. Go out")

    option = int(input("Enter a option: "))

    if option == 1:
        print("Hello...")
    elif option == 2:
        n = float(input("Enter a number: "))
        n **= 2
        print(f"the result is: {n}")
    elif option == 3:
        print("Closing the program....")
    else:
        print("Enter a valid option. Try again")    