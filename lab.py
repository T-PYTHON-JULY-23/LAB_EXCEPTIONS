def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except Exception as e:
    print(e.__class__, e)
else:
    print("the operation is successful")