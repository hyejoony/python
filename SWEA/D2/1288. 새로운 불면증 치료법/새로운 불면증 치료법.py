def sheep_num(N):
    k = 1
    lst = []
    result = 0
    # lst2 = list(map(str, list(range(0,10))))
    while True:
        sheep_num = k * N
        for num in str(sheep_num):
            if num not in lst:
                lst.append(num)
        if len(lst) == 10:
            result = 1
        else:
            k += 1
        
        if result == 1:
            return sheep_num

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc} {sheep_num(N)}')