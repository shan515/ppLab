import math
def func(x):
    return math.exp(float(-x))*((3.2)*math.sin(float(x)) - (0.5)*math.cos(float(x)))
    #return x * x * x - x * x + 2
def bisection(a,b):
    c = a
    while (b-a>0.001):
        c = (a+b)/2
        if func(c)==0:
            print("root is", c)
            break
        elif func(c)*func(a) < 0 :
            b = c
        elif func(c)*func(b) <0 :
            a = c
    return c
print(bisection(-10,20))