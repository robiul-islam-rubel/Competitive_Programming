def a():
    print("Hi this is Rubel from Bangladesh")
a()

def k(x):
    print(x + " Welcoome")

k("Rubel")
k("Hasan")
k("Galib")

def kire(fname,lname):
    print(fname+" "+lname)
kire("Robiul","Islam")
kire("Frank","Wood")
kire("Virat","Kohli")


def fun(*a):
    print("The youngest child is "+ a[0])
fun("Galib","Sifat","Safa")
def fn(a,b,c):
    print("The Youngest child is "+ c)

    fn(a="Safa",b="Sifat",c="Galib")

def rec(a):
    if a>0 :
        result=a+rec(a-1)
        print(result)
    else:
        result=0
    return result
rec(6)