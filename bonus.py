def celsius_to_fahrenheit (celsius) :
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius (fahrenheit):
    return (fahrenheit - 32) * 5/9 

def main():
  while True:
       input_str = input("Enter temperature and unit (e.g., '25 C' or '77 F'): ")
       input_list = input_str.split()
       if len(input_list) != 2:
           print("Invalid input format. Please enter the temperature and unit separated by a space.")
           return 
        try:
           temperature = float(input_str[0])
           unit = input_str[1].upper

           if unit =='F':
               celsius= fahrenheit_to_celsius(temperature)
               print(f"Temperature in Celsius: {celsius} {unit}")
           elif unit == 'C':
               fahrenheit = celsius_to_fahrenheit(temperature)
               print(f"Temperature in fahrenheit: {celsius} {unit}")
           else:
               print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Invalid temperature value. Please enter a valid number.")

        except TypeError as te :
             print(te)
         
main()