# 입력 : 우선순위 배열, 알고싶은 애의 처음 위치(인덱스값)
# 출력 : 실행순서

# 아이디어 : 
# 1. priorities : [[인덱스값, 우선순위]] 리스트로 변환
# 2. orders = [[인덱스값, 우선순위]] #실행순서 담을 리스트
# 3. 본문 실행 규칙 
# 1) while priorites:
# -- 꺼낸 프로세스 하나가 큐 대기중 프로세스 우선순위보다 높다면 방금꺼낸거 append 
# -- 없으면 orders에 순서를 기록한다
# -- 숫자 넣을 때 cnt 포인터 +1 
# -- if 방금 넣은 숫자의 인덱스값이 location값과 같니?
# ---  return cnt 포인터

# 25분^_^
from collections import deque

def solution(priorities, location):
    cnt = 0
    new_priorities = deque([])

    # priorities 재정비. [인덱스값, 우선순위]
    for idx,v in enumerate(priorities):
        new_priorities.append([idx,v])
        
    # print(new_priorities)
        
    # 본문에 기재된 실행 규칙  
    while new_priorities:
        current = new_priorities.popleft()
        
        # 현재 뽑은 프로세스보다 더 우선순위가 높은 프로세스가 있는가?
        # - 있다면
        if any(current[1] < next[1] for next in new_priorities):
            new_priorities.append(current)
            
        # - 없다면 다시 대기큐에 넣기
        else:
            cnt += 1
            if current[0] == location:
                return cnt

    else:

        return cnt
        
priorities = [2, 1, 3, 2]	
location = 2

print(solution(priorities,location))