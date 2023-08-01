def celsius_to_fahrenheit(celsius):
    fahrenheit = round((celsius * 9/5) + 32, 2)
    return f"{fahrenheit} F"

def fahrenheit_to_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5/9, 2)
    return f"{celsius} C"

def main():
    while True:
        try:
            temperature = input("Enter a temperature and its unit (e.g., \"25 C\" or \"77 F\") : ")
            print("if you want to exit enter [-1] ")
            if temperature == "-1":
                break

            unit = temperature[-1].lower()
            temperature_val = temperature.split(" ")[0]
            
        
            if not temperature_val.isdigit():
                raise ValueError(f"'{temperature}' : '{temperature_val}' is not a number")

            if unit == "f":
                print("Temperature in Celsius: ", fahrenheit_to_celsius(float(temperature_val)))
            elif unit == "c":
                print("Temperature in Fahrenheit: ", celsius_to_fahrenheit(float(temperature_val)))
            else:
                raise TypeError(f"'{temperature}' : this '{unit}' should be the unit but it's not")
            
            
        
        except TypeError as t:
            print(t)
        except ValueError as v:
            print(v)


main()