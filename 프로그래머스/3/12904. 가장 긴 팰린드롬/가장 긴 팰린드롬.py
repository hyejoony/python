def solution(s):
    def palin_check(s):
        max_len = 1

        #배열 앞에서부터 탐색(슬라이싱)
        for start in range(0, len(s)):
            end = len(s) #슬라이싱 끝점

            while (end-start) > max_len: #end는 1까지(에러방지)
                #회문 검사 시작
                for i in range((end-start)//2):

                    # 회문이 아니면
                    if s[start+i] != s[end-i - 1]:
                        end -= 1 # 더 작은 부분문자열을 만든다
                        break

                else: #회문이면
                    curr_len = end-start
                    if curr_len > max_len:
                        max_len = curr_len
                        break
    
        return max_len
    answer = palin_check(s)
    return answer