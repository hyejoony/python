
n = int(input())
for i in range(n,0,-1):
    if i == 1:
        print(" "*(n-i) + "*"*(2*i-1),end='')
    elif i != 1:
        print(" "*(n-i) + "*"*(2*i-1))

    
