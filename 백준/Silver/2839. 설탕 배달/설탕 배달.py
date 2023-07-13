n = int(input())
cnt=0 #봉지 수
while n >= 0 : 
    if n%5 == 0:
        a = n // 5
        cnt = cnt + a
        print(cnt)
        break
    n=n-3 #5의 배수가 될 때까지 빼준다
    cnt=cnt+1
else:
    print(-1)