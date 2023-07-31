
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


try:
    additoin(10,20)
 
except  NameError as e:
    print("the error is",e)
   

else:
    print("the operation is successful")

finally:
    print("the program is running")
    