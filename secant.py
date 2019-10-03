import math
def func(x):
    return x**3-20
def secant(a,b):
    h = 1
    flag = 0
    while h >= 0.00001 :
        h = abs(b-a)/b
        flag +=1
        e = (func(a)-func(b))/(a-b)
        a = b
        b = b-func(b)/e

    print("root is ", a)
    print("counter", flag)
    print("error",h)
secant(2,3)