
def solution(s):
    lst = []
    answer = True
    for i in s:  # i == ()
        if i == "(":
            lst.append(i) # lst =["("]
        elif i == ")" and lst != []:
            lst.pop() # lst = []
            
        elif i == ")" and lst == []:
            answer = False
            
    if lst != []:
        answer = False

    return answer

