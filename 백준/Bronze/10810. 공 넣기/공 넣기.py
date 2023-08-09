n,m = map(int,input().split())
lst = [0 for _ in range(n)]
#lst = [0,0,0,0,0]
for _ in range (m): #4번 던져
    i,j,k = map(int,input().split())#1~2번까지 3번공을 다 넣어
    for a in range(i-1,j): #i =1, j = 2
        lst[a] = k #a = 0, 1 # 3

for r in lst:
    print(r,end =' ')