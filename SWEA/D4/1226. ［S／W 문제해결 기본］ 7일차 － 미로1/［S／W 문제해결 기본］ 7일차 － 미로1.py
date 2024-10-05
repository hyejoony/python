from collections import deque

T = 10
for tc in range(1,T+1):
    dum = int(input()) #쓰레기 변수
    N = 16
    matrix = [list(map(int, input())) for _ in range(16)]

    visited = [[0 for _ in range(16)] for _ in range(16)]

    dir = [[-1,0], [1,0], [0,-1], [0,1]] #상하좌우

    answer = 0
    q = deque()
    q.append([1,1]) #출발점 정의
    visited[1][1] = 1  #출발점 방문표시

    while q: 
        #현재 위치 좌표 파악
        coor_pop = q.popleft()
        cur_r, cur_c= coor_pop[0], coor_pop[1]

        # 도착했나요?
        if matrix[cur_r][cur_c] == 3:
            answer = 1
            break
    
        #도착안했으면 4방향 탐색 
        #인접 노드 탐색(4방향)
        for dr,dc in dir:
            nr,nc = cur_r + dr, cur_c + dc 
            if 0 <= nr < N and 0 <= nc < N:
                #방문한적없고 길인 경우에만 담는다
                if not visited[nr][nc] and (matrix[nr][nc] == 0 or matrix[nr][nc] == 3):
                    q.append([nr,nc])
                    visited[nr][nc] = 1 #방문표시

    print(f'#{tc}', answer)
