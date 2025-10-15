"""
Basic calculator
My first program in GitHub
Date: 14/10/2025
Author: Mathiu Osorio(MatzapAI)
"""

print("---CALCULATOR---")

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))

print("---OPTIONS MENU---")
print(" [1] Addition")
print(" [2] Subtraction")
print(" [3] Multiplication")
print(" [4] Division")
print(" [5] Power\n")

option = input("Enter the operation you want to operate: ")

if option == "1":
    num1 += num2
    print(num1)
elif option == "2":
    num1 -= num2
    print(num1) 
elif option == "3":
    num1 *= num2
    print(num1) 
elif option == "4":
    if num2 == 0:
        print("cannot be divided by zero") 
    else:
        num1 /= num2
        print(num1)
elif option == "5":
    num1 **= num2 
    print(num1)
else:
    print("X invalid operation")
    
print("-------------------------------------------")    



