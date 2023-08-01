def celsius_to_fahrenheit( celsius):
    fahrenheit = round((celsius * 9/5) + 32 , 2)
    print("Temperature in Fahrenheit:", fahrenheit)
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5/9 , 2)
    print("Temperature in Celsius:",celsius)
    return celsius
#temperature = float(input("Enter a temperature and its unit (e.g., 25 C or 77 F): "))
def main():
            tempc = celsius_to_fahrenheit(temperature)
            temp = fahrenheit_to_celsius(temperature)
    

try:
        temperature = float(input("Enter a temperature and its unit (e.g., 25 C or 77 F): "))
except ValueError:
    print("invalid temperature value, Please try again")
except TypeError:
    print("Invalid temperature unit. Please try again")
except:
    print("Please try again")

main()