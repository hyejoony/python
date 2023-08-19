
check = False # 확인은~
n = input() #string으로 인풋 #예시 : 1236
#1-236, 12-36, 123-6으로 나눠보기 #slicing활용
for i in range(1,len(n)): #i =1, 2,3,
    front_sliced_num = n[:i]
    # i = 1일 때 변수값은 1236 중 1 # i = 2일 때 변수값은 1236 중 12 #i = 3일 때 변수값은 123
    back_sliced_num = n[i:]
    # i=1일 때 변수값은 1236중 236 # i= 2일 때 변수값은 1236 중 36 # i =3일 때 변수값은 6
    # range 1로 시작하는 이유는
    # 슬라이싱에서 숫자는 0부터있고 1전까지의 값 설정-> 0 나옴으로써
    # 인덱스 0에 접근 가능
    #print(front_sliced_num,back_sliced_num) #확인 #print에서 ,(콤마)는 공백 역할
    gob_num1 = 1 #초기화 방지!
    gob_num2 = 1
    for num_pop1 in front_sliced_num:  # front_sliced_num = 1
        #num_pop1 = 1
        gob_num1 *= int(num_pop1) # 1*1
    for num_pop2 in back_sliced_num: #back_sliced_num = 236
        #num_pop2 = 2, 3, 6
        gob_num2 *= int(num_pop2) # 2*3*6
    if gob_num1 == gob_num2:
       check = True
       break
if check == True:
    print("YES")
else:
    print("NO")