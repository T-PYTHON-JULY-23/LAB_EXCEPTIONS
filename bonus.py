# Instructions:
# Write a function celsius_to_fahrenheit(celsius) that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit. Use the formula fahrenheit = (celsius * 9/5) + 32.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit,2)
# Write a function fahrenheit_to_celsius(fahrenheit) that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius. Use the formula celsius = (fahrenheit - 32) * 5/9.
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,2)

# Write a main function that: 
# a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F").
# b. Splits the input string into a temperature value and its unit.
# c. Tries to convert the input temperature to its opposite unit using the appropriate function (e.g., if the user enters a Celsius temperature, convert it to Fahrenheit).
# d. Handles the following exceptions:
# - ValueError: If the user enters an invalid temperature value, display an error message and prompt the user to try again. 
# - TypeError: If the user enters an invalid unit, display an error message and prompt the user to try again.
# e. If the conversion is successful, print the converted temperature and its unit.
def main_function():
    while True:
        try: 
            tempe_input = input("enter a temperature: 'F'fahrenheit or 'C'celsius :")
            tempe_value , tempe_unit = tempe_input.split()
            if tempe_unit.upper() == 'C':
                celsius = float(tempe_value)
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"temp in fahrenheit: {fahrenheit} F")
                break
            elif tempe_unit.upper() == 'F':
                fahrenheit = float(tempe_value)
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"temp in celsius: {celsius} C")
                break
        except ValueError:
              print("Invalid temperature value. Please enter a valid number.")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
main_function()