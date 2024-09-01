T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #N : 돌 수 # M: 뒤집기 횟수

    #초기상태
    rock_arr = list(map(int,input().split()))
    N = len(rock_arr) #인덱스 벗어나는지 파악 위함


    for _ in range(M):
        i,j = map(int,input().split()) #i번째 돌, 마주보는 j개

        stand_idx= i-1 #기준돌
        for  k in range(1,j+1): #1개, 2개, j+1개 고려
            #인덱스 고려('주어진 돌을 벗어나는 경우 뒤집기는 중지된다.')
            #벗어나지 않는 경우
            if 0<= stand_idx-k<N and 0<= stand_idx+k<N :

                if rock_arr[stand_idx-k] == rock_arr[stand_idx+k]:
                    if rock_arr[stand_idx - k] == 1:
                        rock_arr[stand_idx - k], rock_arr[stand_idx+k] = 0,0
                    else:
                        rock_arr[stand_idx - k], rock_arr[stand_idx + k] = 1,1
                else:
                    continue #다르면 뒤집지 않고 그대로 둔다
            # 인덱스 벗어나는 경우
            else:
                break


    print(f'#{tc}',*rock_arr)
