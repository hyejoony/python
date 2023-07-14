
#빈 배열을 하나 준비해서 9개의 값을 입력받아 넣어줌
#첫째줄에 값 0 개를 9개 줄로 입력하고 싶을 때 
n = []
for _ in range(9):
    n.append(int(input()))
#한 배열 내에서 값을 순차적으로 비교할 때 = 구구단과 유사
n.sort()
result = sum(n)

for i in range(9):
    for j in range(i+1,9):
        if result - n[i] - n[j] == 100:
            for k in range(9):
                if k == i or k== j:
                    continue
                else:
                    print(n[k])
            exit()