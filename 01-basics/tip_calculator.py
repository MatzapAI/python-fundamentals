print("---TIP CALCULATOR---")

tip10 = 0.10
tip15 = 0.15
tip20 = 0.20

amount = float(input("Please enter the amount of your account: "))
print("Thank you for your purchase.")

print("you want to add a tip?")
option = input("yes[Y] no[N]: ")
option = option.lower()

if option == "y":
    print("what percentage do you want to give: ")
    print("Options: \n[a]10% \n[b]15% \n[c]20% \n[d]custom")
    option_tip = input("Select option: ").lower()
    
    tip_percent = 0  
    
    if option_tip == "a":
        tip_percent = tip10
        print("you selected 10%")
    elif option_tip == "b":
        tip_percent = tip15
        print("you selected 15%")
    elif option_tip == "c":
        tip_percent = tip20
        print("you selected 20%")
    elif option_tip == "d":
        print("you selected custom tip")
        custom_tip = float(input("enter your desired tip (%): "))
        tip_percent = custom_tip / 100
    else:
        print("Invalid option, no tip added.")
        tip_percent = 0
    
    tip_amount = amount * tip_percent
    total_price = amount + tip_amount
    
    print(f"\nBill: ${amount:,.2f}")
    print(f"Tip ({tip_percent*100:.0f}%): ${tip_amount:,.2f}")
    print(f"Total: ${total_price:,.2f}")
    print("Thank you for your purchase...")