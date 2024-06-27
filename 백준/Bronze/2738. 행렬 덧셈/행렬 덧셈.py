N,M = map(int,input().split())

matrix_1 = [[0 for i in range(M)] for _ in range(N)]
#행렬 a 초기화
matrix_2 = [[0 for i in range(M)] for _ in range(N)]
#행렬 b 초기화
matrix_3 = [[0 for i in range(M)] for _ in range(N)]
#a+b 계산 행렬 초기화

#matrix
#[[0,0,0]
#[0,0,0]
#[0,0,0]]

#행렬a
for i in range(N): #0,1,2
    oneso = list(map(int, input().split()))
    #oneso = [1,1,1]
    for j in range(M): 
        # i=0일때 j = 0,1,2
        matrix_1[i][j] = oneso[j]
        #matrix_1[0][0] = oneso[0]
        # j =1일때
        #matrix_1[0][1] = oneso[1]
        # j =2일때
        #matrix_1[0][2] = oneso[2]

#행렬b
for a in range(N):
    oneso_2 = list(map(int, input().split()))
    for b in range(M):
        matrix_2[a][b] = oneso_2[b]


#행렬a+b
for z in range(N): 
    for y in range(M):
        matrix_3[z][y] = matrix_1[z][y] + matrix_2[z][y]

#답 출력
for x in range(N):
    for z in range(M):
        print(matrix_3[x][z], end=' ')
    #x = 0, z = 0,1,2 한바퀴 돌고(출력하고)
    print()
    
    


        










