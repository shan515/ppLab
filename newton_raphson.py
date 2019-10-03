import math
from sympy import Symbol, Derivative
global c
def func(x) :
    return x**3-x**2+2
    #return math.exp(float(-x)) * ((3.2) * math.sin(float(x)) - (0.5) * math.cos(float(x)))
def derivFunc(x):
    return 3*x**2-2*x

def newtonRaphson(x):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x) / derivFunc(x)
        x = x - h

    print("The value of the root is : ", "%.4f" % x)
x0 = -2
newtonRaphson(x0)

