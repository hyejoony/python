from collections import deque

def solution(prices):
    price_q = deque(prices) #큐 변환
    
    answer = [] 
    
    while price_q: #대기 큐 빌 때까지
        cnt = 0 
        cur_price = price_q.popleft()
        
        for next_price in price_q:
            cnt += 1
            if cur_price <= next_price :
                continue
            else:
                break
        # 끝까지 떨어지지 않는 경우
        answer.append(cnt) 
    
    return answer