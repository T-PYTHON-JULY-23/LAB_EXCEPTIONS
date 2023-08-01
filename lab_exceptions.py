def additoin(x, y):
  
        x = 10
        y = 20
        print("Addition:", x + b)
  
try:
    additoin(10, 20)
except NameError as e:
     print("The variable is not defined", e, e.__class__)
except:
    print("something went rong")
else:
    print("the operation is successful")
finally:
     print("Finally is run regardless if operation inside try is succsseeded or failed")

