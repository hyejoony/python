n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i+" ")
for j in range(n,1,-1): 
    #print(j,end="")
    if j ==1:
        print(" "*(n-j+1)+"*"*(j-1)+" ",end="")
    elif j != 1:
        print(" "*(n-j+1)+"*"*(j-1)+" ")


n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i+" ")

for j in range(n,1,-1): 
    #print(j,end="")
    print(" "*(n-j+1)+"*"*(j-1)+" ",end="") # 3-1= 2번 실행

    if j != 2:
        print("") #제어를 걸어야 할 때 if를 쓰라~ # 3-2= 1번 실행
