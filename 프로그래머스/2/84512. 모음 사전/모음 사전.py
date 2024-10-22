def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    global answer 
    answer = 0 

    def dfs(string):
        global answer 
        answer += 1  # 새로운 단어를 만들 때마다 카운트 증가
        
        # 목표 단어를 찾으면 True 반환
        if string == word:
            return True
        
        # 단어 길이가 5가 되면 더 이상 확장하지 않고 False 반환
        if len(string) == 5:
            return False
        
        # 현재 단어에 각 모음을 추가하여 새로운 단어 생성
        for alpha in alphabets:
            # 새로운 단어로 재귀 호출, True가 반환되면 목표 단어를 찾은 것
            if dfs(string + alpha) == True:
                return True 
        
        # 모든 모음을 시도해도 목표 단어를 못 찾으면 False 반환
        return False

    # 각 모음으로 시작하는 단어에 대해 DFS 수행
    for alpha in alphabets:
        if dfs(alpha) == True:
            return answer
