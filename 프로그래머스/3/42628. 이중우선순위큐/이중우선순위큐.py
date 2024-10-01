# 프로그래머스 이중우선순위큐


# 11:21 -48분 :27분캬캬아아아아아

# 입력 : 리스트(문자열,문자열,)
# 출력 : [최대,최소] 
#  - 큐 비어있으면 [0,0]


# 아이디어 : I면 큐에 넣고 D면 최소 혹 최대 찾아서 삭제
# 1. 문자열 순회하여 조건에 따라 처리
# - (1) 문자열의 첫번째가 s[0] == I이면
# -- 공백 기준으로 분리 -> 숫자에 해당되는 lst[-1]을 큐에 넣는다
# - (2) 문자열이 D 1이면
# *que가 비어있지 않을 때만 아래 실행*
# -- 큐를 최대힙으로 정렬, 최대값 삭제
# - (3) 문자열이 D -1이면
# *단, 최대힙 -> 최소힙 재정렬일때는 - -> + 로 변환후 최소힙 정렬 필요*
# ---> 놉! 최대힙 정렬 후 최댓값 찾고 - 부호 다시 취해주면 됨 ㅋ
# -- 큐를 최소힙으로 정렬, 최솟값 삭제
# 2.순회를 마쳤을 때, 
# -- que가 비어있지 않을 때 최소,최대값 찾는다
# --  que가 비어있으면 최소 최대 0으로


import heapq

def solution(operations:list):
    q =[]
    for oper in operations:
        if oper[0] == 'I':
            lst = oper.split()
            #큐에 넣는다 : 일단 최소힙으로 만들어도 ㄱㅊ을듯
            q.append(int(lst[-1])) #?heappush 아니라고? 왜 됨?
        elif q and oper == 'D -1':
            heapq.heapify(q)
            #최소값 삭제 및 반환
            min_val = heapq.heappop(q)
                
        elif q and oper == 'D 1':
            #최대힙으로 재정렬
            q = [-x for x in q]
            heapq.heapify(q)
            #최대값 삭제 및 반환
            max_val = -heapq.heappop(q)
            q = [-x for x in q]
    #순회 다 마치고
    #q 비어있지않을 때 최소, 최대값 찾기
    if q:
        min_val = min(q)
        max_val = max(q)
        return [max_val,min_val]
    else:
        return [0,0]

                 
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	
print(solution(operations))
