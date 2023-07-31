def additoin(x, y):
  
        x = 10
        y = 20
        print("Addition:", x + b)
  
try:
    additoin(10, 20)
except Exception as e:
     print("error", e, e.__class__)
else:
    print("the operation is successful")
finally:
     print("Finally is run regardless if operation inside try is succsseeded or failed")

