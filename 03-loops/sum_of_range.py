print("---SUM OF RANGE---")

num1 = int(input("Enter a firts number: "))
num2 = int(input("Enter a second number: "))

sum = 0

for i in range (num1, num2 + 1):
    sum += i
print(f"Sum: {sum}")        