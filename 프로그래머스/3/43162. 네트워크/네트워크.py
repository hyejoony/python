from collections import deque

G = [[] for _ in range(100)]
vis = [False] * 100

def bfs(node):

    # initialization 
    q = deque([node])
    vis[node] = True

    # main logic : BFS 
    while q:
        cur = q.popleft()
        for nxt in G[cur]:
            if not vis[nxt]:
                vis[nxt] = True
                q.append(nxt)

    return vis 

def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                G[i].append(j)
                G[j].append(i)

    for i in range(n):
        if not vis[i]:
            bfs(i)
            answer+=1

    return answer