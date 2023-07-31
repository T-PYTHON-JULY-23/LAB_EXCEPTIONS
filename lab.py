def addition(x, y):
    try:
        x = 10
        y = 20
        result = x + y
        print("Addition:", result)
        print("The operation is successful")
    except NameError:
        print("Error: The variable 'b' is not defined.")


addition(10, 20)


#---------------------second solve: -------------

def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10,20)

except TypeError:
    print(" the error")
else:
    print("successful")
finally:
    print("the proram is running")