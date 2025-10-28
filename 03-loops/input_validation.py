print("---INPUT VALIDATION---")

while True:
    input_age = input("Enter your age: ")
    
    if input_age.isdigit():
        age = int(input_age)
        
        if 0 <= age <= 120:
            if age < 18:
                print("You are a minor.")
            else:
                print("You are a adult.")
            break
        else:
            print("Invalid range age. Try again.")
    else:
        print("Invalid input. Please enter digits only.") 

   