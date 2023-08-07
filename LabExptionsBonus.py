def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        temp_input = input("Please enter the temperature and its unit (C or F) separated by a space:")
        temp_list = temp_input.split()
        
        try:
            temperature = float(temp_list[0])
        except ValueError:
            print("Invalid temperature value. Please try again.")
            continue
        
        if temp_list[1].upper() == 'F':
            try:
                converted = fahrenheit_to_celsius(temperature)
            except TypeError:
                print("Invalid temperature unit. Please try again.")
                continue
            print("{} F is equivalent to {} C.".format(temperature, converted))
            break
            
        elif temp_list[1].upper() == 'C':
            try:
                converted = celsius_to_fahrenheit(temperature)
            except TypeError:
                print("Invalid temperature unit. Please try again.")
                continue
            print("{} C is equivalent to {} F.".format(temperature, converted))
            break
        
        else:
            print("Invalid temperature unit. Please try again.")
            continue
        
if __name__ == '__main__':
    main()