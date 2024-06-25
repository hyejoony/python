N , K = map(int, input().split())
room_cnt = 0 #방 수
grl_lst = [] #여자성별 담을 리스트
boy_lst = [] #남자 담을 리스트

for _ in range(N): #16번 반복
    S, Y = map(int, input().split())
    
    #여자일때 남자일때 우선 구분
    if S==0: 
        grl_lst.append(Y)
    else:
        boy_lst.append(Y)

    

#여자 남자별 학년별 명수 카운트
total_grl_lst = []

grl_1 = grl_lst.count(1)
grl_2 = grl_lst.count(2)
grl_3 = grl_lst.count(3)
grl_4 = grl_lst.count(4)
grl_5 = grl_lst.count(5)
grl_6 = grl_lst.count(6)

for i in [grl_1, grl_2, grl_3, grl_4, grl_5, grl_6]:
    total_grl_lst.append(i)

   

#남자 파악
boy_1 = boy_lst.count(1)
boy_2 = boy_lst.count(2)
boy_3 = boy_lst.count(3)
boy_4 = boy_lst.count(4)
boy_5 = boy_lst.count(5)
boy_6 = boy_lst.count(6)
total_boy_lst = []

for i in [boy_1, boy_2, boy_3, boy_4, boy_5, boy_6]:
    total_boy_lst.append(i)
    

#최소 필요 방 수 확인
#K : 방별 제한 인원수 
for i in total_grl_lst:

    if i !=0  and i < K: #최대인원 보다 적은 학년 명수라면, 방 하나 주기 
        room_cnt += 1

    elif i == 0: #0명이면 지나가고
        pass
        
    elif i !=0 and i >= K: # 최대인원수 보다 많다면
        mok = i  // K
        nameoji = i  % K
    
        if nameoji != 0:
            sum = mok + 1
            room_cnt += sum
        else:
            room_cnt += mok


for i in total_boy_lst:
    #print(i)

    if i !=0  and i < K: #최대인원 보다 적은 학년 명수라면, 방 하나 주기 
        room_cnt += 1

    elif i == 0: #0명이면 지나가고
        pass
        
    elif i !=0 and i >= K: # 최대인원수 보다 많다면
        mok = i  // K
        nameoji = i  % K
    
        if nameoji != 0:
            sum = mok + 1
            room_cnt += sum
        else:
            room_cnt += mok

print(room_cnt)  
        

        
        
    


