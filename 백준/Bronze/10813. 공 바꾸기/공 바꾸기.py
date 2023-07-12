n,m = map(int,input().split())
result = [z for z in range(1,n+1)] #리스트 완성
for _ in range(m):
	i,j = map(int,input().split())
	result[j-1], result[i-1]=result[i-1], result[j-1] 
	        
for e in result:
	print(e,end=' ')
