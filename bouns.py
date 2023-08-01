
#Write a function celsius_to_fahrenheit(celsius) that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit. 


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    
    return fahrenheit 


#Write a function fahrenheit_to_celsius(fahrenheit) that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius.
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9.
    return celsius



try:
    user_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F")')
    degree = int(user_input[:-1])
    i_convention = user_input[-1]
    if i_convention.upper() == "C":
        print(f"Temperature in Celsius:{celsius_to_fahrenheit()}") 
    elif i_convention.upper() == "F":
        print("Temperature in fahrenheit:" , fahrenheit_to_celsius())
except ValueError as e:
    print("Invalid value try agien")
except TypeError as e:
    print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
except Exception as e:
    print("Somthing is wrong")







