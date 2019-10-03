n = 4
m =1
for i in range(0,4):
    for j in range(0,n):
        print(" ",end=" ")
    for k in range(65,65+m):
        a = chr(k)
        print(a,end=" ")
    m = m+2
    n =n-1
    print( )