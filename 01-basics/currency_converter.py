"""
date: 1/10/2025
price of EUR and USD today:
1 USD = 3851.75
1 EUR = 4494.80
"""


print("---CURRENCY CONVERTOR---")

print("Select your currency: ")

print("Peso colombiano [COP] \nUS dolar [USD] \nEuro [EUR]")

print("Digit your type currency")
print("Example: cop")

type_currency = input("option: ")
type_currency = type_currency.lower()

if type_currency == "cop":
    print("\nCurrency converter\n")
    print("[1] COP --> USD \n[2] COP --> EUR")
    
    option = int(input("Select a option: "))
    
    if option == 1:
        
        print("You have selected the conversion from COP to USD.")
        start_amount = amount = float(input("Enter your amount in COP: "))
        
        amount /= 3.852 

        print(f"its amount of {start_amount}COP in dollar is: {amount:.3f}")     
    elif option == 2:
        
        print("You have selected the conversion from COP to EUR.")
        start_amount = amount = float(input("Enter your amount in COP: "))
        
        amount /= 3.852 

        print(f"its amount of {start_amount}COP in EUR is: {amount:.3f}") 
    else:
        print("X option no valid.")
        print("Close the program...")  
elif type_currency == "usd":
    
    print("\nCurrency converter\n")
    print("[1] USD --> COP \n[2] USD --> EUR")
    
    option = int(input("Select a option: "))
    
    if option == 1:
        
        print("You have selected the conversion from USD to COP.")
        start_amount = amount = float(input("Enter your amount in USD: "))
        
        amount *= 3851.90

        print(f"its amount of {start_amount}USD in peso Colombiano is: {amount:.3f}")     
    elif option == 2:
        
        print("You have selected the conversion from USD to EUR.")
        start_amount = amount = float(input("Enter your amount in USD: "))
        
        amount *= 0.86

        print(f"its amount of {start_amount}COP in EUR is: {amount:.3f}") 
    else:
        print("X option no valid.")
        print("Close the program...")         
elif type_currency == "eur":
    print("\nCurrency converter\n")
    print("[1] EUR --> COP \n[2] EUR --> USD")
    
    option = int(input("Select a option: "))
    
    if option == 1:
        
        print("You have selected the conversion from EUR to COP.")
        start_amount = amount = float(input("Enter your amount in EUR: "))
        
        amount *= 4494.80

        print(f"its amount of {start_amount}EUR in peso Colombiano is: {amount:.3f}")     
    elif option == 2:
        
        print("You have selected the conversion from EUR to USD.")
        start_amount = amount = float(input("Enter your amount in EUR: "))
        
        amount *= 1.17

        print(f"its amount of {start_amount}EUR in USD is: {amount:.3f}") 
    else:
        print("X option no valid.")
        print("Close the program...")     
else:
    print("X option no valid.")
    print("Close the program...")         