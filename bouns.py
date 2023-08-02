def main():


    while True:
        try:
            user_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F")')
            temp , unit = user_input.split()
            temp = float(temp)
            if unit.upper() == "C":
                print("temperature in celsius", celsius_to_fahrenheit(temp))
            elif unit.upper()== "F":
                print("temperature in fahrenheit", fahrenheit_to_celsius(temp))
            else:
                raise TypeError("We accept only F for fahrenheit or C for celsius")
        except ValueError:
            print("Please only enter number ")
        except TypeError as e:
            print(e)


main()
