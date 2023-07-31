''' Program Temperature Converter '''




def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(f"Temperature in Celsius : {round(celsius,2)} C\n")


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit} F\n")

user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
def main():
    if user_input.endswith("F"):
        num1 = user_input.split()
        del num1[1]
        for num in num1:                
            int_num = float(num)
            fahrenheit_to_celsius(int_num)

    elif user_input.endswith("C"):
        num1 = user_input.split()
        del num1[1]
        for num in num1:
            int_num = float(num)
            celsius_to_fahrenheit(int_num)
    else:
        b=""
        x=b+1
try:
     main()
except TypeError:
    print("Please try again")
except ValueError:
    print("Please write the number of the temperature..")
except Exception as e:
    print(e.__class__)
else:
    print(main())