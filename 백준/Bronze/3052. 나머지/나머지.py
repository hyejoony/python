
lst = []
for _ in range(10):
    n = int(input())
    
    a = n % 42 
    if a not in lst:
        lst.append(a)
print(len(lst))
