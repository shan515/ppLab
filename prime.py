from math import *

x = int(input("Enter no"))
#for i in range(1, x):
for z in range(2, x):
    y = x % z
    if y == 0:
        print(x, " Not prime")
        break
    else:
        print(x, " Prime nos")
        break
