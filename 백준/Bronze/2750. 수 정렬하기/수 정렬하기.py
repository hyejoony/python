n = int(input())
lst = []
for _ in range(n):
     a = int(input())
     lst.append(a)

lst.sort()   
for i in lst:
     print(i)