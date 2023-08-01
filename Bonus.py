
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    units_C= 'C'
    units_F= 'F'
    Conversion = 0
    Conversion_str =""

    try:
        User_Choice = input("Enter a temperature and its unit (either C for Celsius or F for Fahrenheit), separated by a space (e.g., 25 C or 77 F): ")
        

    except TypeError: 
        if User_Choice[1] != units_F and User_Choice[1] != units_C:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            pass
    except ValueError: 
        if User_Choice[0].isnumeric():
            print("Invalid value. Please use number value.")
    Temperature_Value_Unit= User_Choice.split(" ")
    Tepval= int(Temperature_Value_Unit[0])
    if User_Choice[1] == units_C:
        Conversion = celsius_to_fahrenheit(Tepval)
        Conversion_str= str(Conversion) +' F'
            
    if User_Choice[1] == units_F:
        Conversion = fahrenheit_to_celsius(Tepval)
        Conversion_str= str(Conversion) +' C'
         

    print(f"Converting {User_Choice} to its opposite unit : {Conversion_str} ")


main()