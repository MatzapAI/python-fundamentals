print("---BMI CALCULATOR---")

heigth_cm = float(input("Enter your height in cm: "))
weigth = float(input("Enter your weigth in Kg: "))

heigth_metros = heigth_cm / 100

bmi_formula = weigth / pow(heigth_metros, 2)

print(f"you have a BMI of: {bmi_formula:.2f}")

if 0 < bmi_formula < 18.5:
    print(f"You have a very low weight in proportion to your height: {heigth_cm}cm")
    print("You need meat more...")
elif 18.5 <= bmi_formula <= 24.9:
    print("You have a normal weight... you are doing well. ")
elif 25 <= bmi_formula <= 29.9:
    print("You're overweight, you have to cut down on the hamburgers. ")  
elif bmi_formula >= 30:    
    print("you have obesity...")
else:
    print("How are you going to have a negative BMI?")
    

    