#아이디어
# 1. 주어진 문자열 s를 순서대로 순회한다
# 2. 여는 괄호를 담을 리스트(스택)을 만든다
# - 여는 괄호이면 스택에 담는다
# - 스택이 비어있고 닫는 괄호면 올바른 괄호가 아니다
# - 스택이 비어있지 않고 닫는 괄호면, 스택에서 (를 하나 뺀다(매칭)
# 3. 문자열 s 순회 다 마쳤는데 stack 안비어있다? 올바른 괄호x
def solution(s):
    lst = []
    answer = True
    
    for small_s in s:
        if small_s == '(':
            lst.append(small_s)
        elif small_s == ')' and lst:
            lst.pop() #짝 매칭
        else:
            answer = False
            return answer
    else:
        if lst:
            answer = False
            
    return answer