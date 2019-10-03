n = 5
m = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    for k in range(0,m):
        print("*",end=" ")
    m =m+1
    n = n-1
    print( )


