n =int(input())
for i in range(1,n+1):
    print(" "*(n-i), "*"*(2*i-1),sep='')
for j in range(n-1,0,-1):
    if j == 1:
        print(" "*(n-j),"*"*(2*j-1),sep='',end='')  
    elif j !=1:   
        print(" "*(n-j),"*"*(2*j-1),sep='')