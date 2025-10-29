print("---PRODUCTS AND PRICE---")

products = ["bread", "milk", "eggs", "rice", "fruit"]
prices = [1.2, 0.9, 2.5, 1.8, 3.0]

for x, y in zip(products, prices):
    print(f"product: {x}, price: {y}")