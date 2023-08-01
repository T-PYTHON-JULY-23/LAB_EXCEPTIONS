
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    Conversion = 0
    #Tepval= int(Temperature_Value_Unit[0])
    while True:
        try: 
            User_Choice = input("Enter a temperature and its unit (either C for Celsius or F for Fahrenheit), separated by a space (e.g., 25 C or 77 F): ")
            if User_Choice == "exit":
                break
            TempValue,TempUnit= User_Choice.split(" ")
            if TempValue.isnumeric():
                TempValue = float(TempValue)
            else:
                raise TypeError("Please only enter numbers.")

            
            if TempUnit.upper() == 'C':
                Conversion = celsius_to_fahrenheit(TempValue)
                Conversion_str= str(Conversion) +' F'
                print(f"Converting {User_Choice} to its opposite unit : {Conversion_str} ")
           
            elif TempUnit.upper() == 'F':
                Conversion = fahrenheit_to_celsius(TempValue)
                Conversion_str= str(Conversion) +' C'
                print(f"Converting {User_Choice} to its opposite unit : {Conversion_str} ")
           
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except TypeError as  e: 
            print(e)
        except ValueError as e: 
            print(e)

main()
