print("---FIZZBUZZ---")

for i in range (1,101):
    output = ""
    if i % 3 == 0:
        output += "fizz"
    if i % 5 == 0:
        output += "buzz"
    #short-circuit evaluation
    print(output or i)    
                 