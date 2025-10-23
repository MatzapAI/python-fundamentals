print("---SUM UNTIL ZERO---")

sum = 0

while True:
    
    nums = float(input("Enter a number: "))
    
    if nums == 0:
        break
    
    sum += nums
    
print(f"the total sum is {sum}")      


