print("---TEMPERATURA CONVERTER---\n")


print("Celsius[C] \nFahrenheit[F] \nKelvin[K] \n")


type_temperature = input("What a type of temperature do you want to convert: ")
type_temperature = type_temperature.lower()
temperature = previous_temperature = float(input("Enter the temperature: "))


if type_temperature not in ["c","f","k"]:
    print("X Option no valid")
else:
    print("What temperature do you want to convert it to?: \n")
    #Celsius conversion
    if type_temperature == "c":
        
        print("Fahrenheit[F] \nKelvin[K]")
        convert = str(input("Select an option: "))
        convert = convert.lower()
        
        if convert == "f":
            temperature = (temperature * 9/5) + 32
            print(f"the temperature: {previous_temperature}°C converted to Fahrenheit is: {temperature}°F")
        elif convert == "k":
            temperature += 273.15
            print(f"the temperature: {previous_temperature}°C converted to Kelvin is: {temperature}°K")
        else:
            print(f"{convert} is not valid")    
    #Fahrenheit conversion     
    elif type_temperature == "f":
        print("Celsius[C] \nKelvin[K]")
        convert = str(input("Select an option: "))
        convert = convert.lower()

        if convert == "c":
            temperature = (temperature - 32) * 5/9
            print(f"the temperature: {previous_temperature}°F converted to Celsius is: {temperature}°C")
        elif convert == "k":
            temperature = (temperature - 32) * 5/9 + 273.15  
            print(f"the temperature: {previous_temperature}°F converted to Kelvin is: {temperature}°K")
        else:
            print(f"{convert} is not valid ")
            
    #Kelvin conversion
    elif type_temperature == "k":
        print("Celsius[C] \nFahrenheit[F]")
        convert = str(input("Select an option: "))
        convert = convert.lower()
        
        if convert == "c":
            temperature -= 273.15
            print(f"the temperature: {previous_temperature}°K converted to Celsius is: {temperature}°C")
        elif convert == "f":
            temperature = (temperature - 273.15) * 9/5 + 32
            print(f"the temperature: {previous_temperature}°K converted to Celsius is: {temperature}°F")
    
    else:
        print("X Option no valid")

   



