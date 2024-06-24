#큐
from collections import deque


def solution(prices):
    prices = deque(prices)
    answer = [] #출력 배열
    while prices: #prices 리스트가 빌 때까지 반복 진행
        a=prices.popleft() #첫번째꺼 빼서 리스트 크기 줄이고
        cnt = 0 
        for i in prices:
            if a <= i:
                cnt += 1

            else:
                cnt+= 1
                break

        answer.append(cnt )
            
                    
    return answer


