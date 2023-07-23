N, M = map(int,input().split())
#N*M 행렬
mat1 =[[0 for _ in range(M)] for _ in range(N)]
mat2 =[[0 for _ in range(M)] for _ in range(N)]
mat3 =[[0 for _ in range(M)] for _ in range(N)]
#[[0,0,0],[0,0,0],[0,0,0]]
#행렬문제는 이중 for문을 돌림
for i in range(N):
    cols = list(map(int, input().split(' ')))
    for j in range(M):
        mat1[i][j] =cols[j] #0,0좌표
for i in range(N):
    cols  = list(map(int, input().split(' ')))
    for j in range(M):
        mat2[i][j] =cols[j]
for i in range(N):
    for j in range(M):
        mat3[i][j] = mat1[i][j]+mat2[i][j]
for i in range(N):
    for j in range(M):
        print(mat3[i][j],end=' ')
    print()