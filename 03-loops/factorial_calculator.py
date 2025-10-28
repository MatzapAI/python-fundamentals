print("---FACTORIAL CALCULATOR---")

num = int(input("Enter a number: "))

factorial = 1

for i in range (1 , num + 1):
    factorial *= i   
    print(factorial)  
print(f"The factorial of {num} is {factorial}")