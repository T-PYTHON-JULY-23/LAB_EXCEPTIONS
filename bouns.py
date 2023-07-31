def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
t = True
while t == True:
    userInput = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
    try: 
        m=len(userInput) - 2
        temp = int(userInput[:m])
        unit= userInput[m+1:]
        if (unit.upper() == 'C'):
            tempF= celsius_to_fahrenheit(temp)
            print(f'Temperature in Fahrenheit: {round(tempF,2)} F')
            t = False
        elif(unit.upper() =='F'):
            tempC= fahrenheit_to_celsius(temp)
            print(f'Temperature in Celsius: {round(tempC,2)} C')
            t= False
        else:
            print('Invalid unit. Please use (C) for Celsius or (F) for Fahrenheit, try again')
    except ValueError as e :
        print(e)
        print('invalid temperature value try again')
    except TypeError as error:
            print(error)
            print('invalid temperature unit try again')