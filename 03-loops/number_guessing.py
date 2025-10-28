import random

print("---NUMBER GUESSING GAME---")

number = random.randint(1,100)

while True:
    n = int(input("Enter a number: "))
    if n == number:
        print("Correct")
        break
    elif n > number:
        print("very high")
    elif n < number:
        print("very low")
