from math import *
#def func1(y,z):
    #return (((17-y)+2*z)/20)

#def func2(x,z):
    #return (((-18+z)-3*x)/20)

#def func3(y,x):
 #   return (((25+3*y)-2*x)/20)

def gauss(y,z):
    x= ((17-y)+2*z)/20
    y = ((-18+z)-3*x)/20
    z = ((25+3*y)-2*x)/20
    return(x,y,z)

flag = 0
y,z = [int(i) for i in input("Enter value of y0 and z0").split()]
a,b,c = gauss(y,z)

while ((20*a+b-2*c)!=17) :
    flag+=1
    temp1 = b
    temp2 = c
    a,b,c = gauss(temp1,temp2)

print("Values are",a,b,c)
print("Iterations are",flag)





