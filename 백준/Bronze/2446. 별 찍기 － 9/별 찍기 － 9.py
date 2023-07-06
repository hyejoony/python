n = int(input())
for i in range(n,0,-1):
    if i == 1:
        print(" "*(n-i)+ "*"*(2*i-1)+ " ")
    elif i != 1:
        print(" "*(n-i)+ "*"*(2*i-1)+" ")
for j in range(2,n+1):
    if j == 5:
        print(" "*(n-j)+ "*" *(2*j-1)," ",end='')
    elif j != 5:
        print(" "*(n-j)+ "*" *(2*j-1)+" ")