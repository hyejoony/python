A,B=map(int,input().split())

#가위바위보
# n이 가위이고 m이 바위일때
# n이 가위이고 m이 보 일때
# 그반대

#가위 1 바위 2 보 3

result = 'A'
#가위일때  
if A  == 1:
    if B == 2:
        result = 'B'

elif B == 1:
    if A == 3:
        result = 'B'

#바위일때
elif A == 2:
    if B == 3:
        result = 'B'

elif B == 2:
    if A == 1:
        result = 'B'

#보일때
elif A == 3:
    if B == 1:
        result = 'B'
elif B == 3:
    if A == 2:
        result = 'B'

print(result)


        