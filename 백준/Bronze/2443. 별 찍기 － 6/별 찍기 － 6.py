n = int(input())
for i in range(0,n):
    print(" "*i + "*"*(2*n-1-(2*i)),sep="")


n = int(input())

for i in range(n, 0, -1):
    # 왼쪽 공백 출력
    print(' ' * (n - i), end='')
    # 별 출력
    print('*' * (2 * i - 1))
    
