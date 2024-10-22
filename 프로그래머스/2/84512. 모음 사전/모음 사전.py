def solution(word):
    words = []
    
    def recur(cur_string):
        if cur_string:  # 빈 문자열이 아닌 경우에만 추가
            words.append(cur_string)
        
        if len(cur_string) == 5:
            return
        
        for next_char in 'AEIOU':
            recur(cur_string + next_char)
    
    recur("")
    return words.index(word) + 1

# # 테스트
# print(solution("AAAAE"))  # 6
# print(solution("AAAE"))   # 10
# print(solution("I"))      # 1563
# print(solution("EIO"))    # 1189