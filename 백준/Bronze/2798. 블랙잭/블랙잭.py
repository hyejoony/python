from collections import deque
import sys
N,M = map(int, sys.stdin.readline().split(' ')) #ex: 5, 21
#카드개수n #카드 3장의 목표 합 m
num_on_card = list(map(int, sys.stdin.readline().split(' ')))
#카드에 쓰여있는 숫자들 입력
# ex : num_on_card = [5,6,7,8,9]

#카드 n개 중 3개의 합이 m에 가까운 경우 찾기
#카드 3장씩 조합을 찾아야해서 삼중 for믄

#경우의 수 다 담아줄 deque(초기화방지/list의 append는 비용이 크다)
deq = deque()
for i in range(0,N):#0~ n까지 #첫째자리
    for j in range(i+1,N): #둘째자리
        for k in range(j+1,N): #셋째자리 등 
            hab = num_on_card[i] + num_on_card[j] + num_on_card[k]
            if hab <= M:
                deq.append(hab)
print(max(deq),end='')



























