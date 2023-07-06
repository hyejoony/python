n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i+" ") #1~3
for j in range(n,0,-1): # 2~1
    if j ==1:
        print(" "*(n-j+1)+"*"*(j-1)+" ",end="")
    elif j != 1:
        print(" "*(n-j+1)+"*"*(j-1)+" ")
