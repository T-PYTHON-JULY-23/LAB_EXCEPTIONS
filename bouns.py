 
def celsius_to_fahrenheit(celsius):
    return round((9 * celsius) / 5 + 32,2)
    
def fahrenheit_to_celsius(fahrenheit):
    return round ((fahrenheit - 32) * 5 / 9,2)




temperature =input(f"Enter a temperature and its unit (e.g., 25 C or 77 F: ").split(" ")
try:
 degree,unit= temperature


 if unit == "C":
  result =celsius_to_fahrenheit(int(degree)) 
  new_U = "F"
  conve="Fahrenheit"
 elif unit == "F":
   result = fahrenheit_to_celsius(int(degree))
   new_U = "C"
   conve= "Celsius"
 print("The temperature in", conve, "is", result,new_U)



except ValueError:
       print("Invalid value. Please .")
 

except  :
    print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    