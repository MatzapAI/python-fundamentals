print("---DISCOUNT CALCULATOR---")

original_price = float(input("Enter the original price in USD: "))
discount = float(input("Enter the discount (Example: 20): "))

if 0 <= discount <= 100:
    total = original_price * (1 - discount / 100)
    print(f"The product originally costs ${original_price:.2f}.")
    print(f"With a {discount:.0f}% discount, the final price is ${total:.2f} USD.")
else:
    print("Invalid discount. Please enter a value between 0 and 100.")