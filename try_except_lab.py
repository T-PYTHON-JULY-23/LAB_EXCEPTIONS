def additoin(x, y):
    try:
        print("Addition:", x + b)
    except NameError as e:
        print("Error: Invalid variable used in the function.")
    else:
        print("the operation is successful")


additoin(10, 20)
