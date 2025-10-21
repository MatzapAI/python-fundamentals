print("---AREA CALCULATOR---")


print("Welcome to area calculator.")
print("handled figures:\nCircle \nRectangle \nTriangle ")
print("Please write the type of figure (example: circle): ")
figure = input("Figure: ")
figure = figure.lower()

if figure == "circle":
    radio = float(input("Enter the radius of the circle: "))
    area = 3.1416 * (radio ** 2)  
else:
    base = float(input("Enter the base of your figure: "))
    height = float(input("Enter the height of your figure: "))
    
    if figure == "rectangle":
        area = base * height 
    elif figure == "triangle":
        area = (base * height) / 2
    else:
        print("X Option no valid")
        area = None

if area is not None:
    print(f"The area of the {figure} is {area}cm². ")
    