print("---AVERAGE OF NUMBERS---")

original_number = quantity_numbers = int(input("Enter the number of numbers you want to add and average: "))
total = 0

while quantity_numbers != 0:
   num = float(input("Enter a number: "))
   total += num
   quantity_numbers -= 1

total /= original_number
print(f"El promedio es: {total}") 
