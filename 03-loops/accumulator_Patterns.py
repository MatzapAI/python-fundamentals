print("---ACCUMULATOR PATTERNS---")

count = 0
nums = 10
list_numeros = []
while nums > 0: 
    n = float(input("Enter a number: "))
    nums -= 1   
    print(f"remaining numbers: {nums}")
    if n > 50:
        list_numeros.append(n)
        count += 1
print(f"numbers greater than 50: {list_numeros}")
print(f"Total count: {count}")

    
    