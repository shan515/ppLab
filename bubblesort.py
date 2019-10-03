import array as a
n=int(input("enter number of elements"))
x=a.array('u',[])
for i in range(n):
        a.append(input("enter the element"))
for j in range(0,n-1):
    for l in range(0,n-1):
        if x[l]>x[l+1]:
            temp=x[l]
            x[l]=x[l+1]
            x[l+1]=temp
for k in x:
    print(k,end=" ")