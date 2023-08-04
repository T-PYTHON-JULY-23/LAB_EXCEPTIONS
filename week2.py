
try:
    def additoin(x, y):
        x = 10
        y = 20
        print("Addition:", x + b)


    additoin(10, 20)
    print(Exception)
except NameError :
    print("'b' is not defined")
except Exception as e:
    print("something went wrong" , e)
else:
    print("the operation is successful")

