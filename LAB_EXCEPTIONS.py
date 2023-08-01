def addition(x, y):
    try:
        print("Addition: ", x + y)
    except NameError:
        print("Error: variable b is not defined")
    else:
        print("The operation is successful")

addition(10, 20)
