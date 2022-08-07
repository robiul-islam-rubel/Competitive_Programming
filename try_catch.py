try:
    print(x)
except:
   print("An Exception error")

try:
    print(x)
except NameError:
    print("Variable is not declerated")
except:
    print("Something else went wrong")
