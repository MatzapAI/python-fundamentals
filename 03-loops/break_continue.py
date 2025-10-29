print("---LOOP OF NUMBERS---")

while True:

    n = int(input("Enter a number (0 to exit): "))

    if n == 0:
        print("Clousing program...")
        break
    if n < 0:
        print("Negative number ignored")
        continue

