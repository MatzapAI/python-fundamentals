print("---GRADE CLASSIFIER---")

note = int(input("Enter your grade (0-100): "))

if note < 0 or note > 100:
    print("the score must be between 0 and 100. ")
else:
    if note >= 90:
        print("Excellent")
    elif note >= 80:
        print("Very good")
    elif note >= 70:
        print("Good")    
    elif note >= 60:
        print("Enough")   
    else:
        print("failed")
         