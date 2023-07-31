



def celsius_to_fahrenheit(celsius):

    fahrenheit = (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9

def main ():
 
    temperature_input = complex(input("Enter a temperature and its unit either C for Celsius or F for Fahrenheit):"))


    if temperature_input == "F" :
      celsius_to_fahrenheit(temperature_input)
      print(f"Temperature in Fahrenheit: {temperature_input} F")

    elif temperature_input == "C" : 
       fahrenheit_to_celsius(temperature_input) 
       print(f"Temperature in Celsius: {temperature_input} C")


try :
    main ()
except ValueError : 
    input("invalid temperature value try again")
except TypeError :
    print("invalid unit try again")