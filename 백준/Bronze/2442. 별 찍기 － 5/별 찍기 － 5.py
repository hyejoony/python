n =int(input())
for i in range(1,n+1):
    print(" "*(n-i)+ "*"*(2*i-1))

a = int(input())
for i in range(1,a+1):
    if a != i:
        print(' '*(a-i) + '*'*(2*i -1))
    elif a == i:
        print(' '*(a-i) + '*'*(2*i -1), end='')#마지막 줄만 엔터를 치지 않겠다
