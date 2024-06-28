# 별 (4)> 동그라미(3) > 네모(2) > 세모 (1)
# 넷 모두 같으면 무승부 D 

#리스트 , count(), 각각 변수 비교

#4, 3, 2, 1의 순서대로 주어지지 않을 수 있음에 주의하라.

N = int(input())#총 라운드 수

for _ in range(N):
    ##라운드 1
    A_card = list(map(int,input().split()))
    #a = 1라운드에서 A가 낸 딱지 그림 수 
    # b는 딱지 위 그림 종류 숫자들
    
    list_A = [] ## 카드 종류들만 따로 담아두기
    # ## 카드 종류들만 따로 담아두기
    for i in A_card[1:]:

        list_A.append(i)



    B_card = list(map(int, input().split()))
    # c = 1라운드에서 B가 낸 딱지 위 그림 수
    # 딱지 위 그림 종류 숫자들
    list_B = []
    for i in B_card[1:]:
        
        list_B.append(i)   


    ##비교 대결 스따또

    # A가 별 카드 갯수가 더 많다면 끝난 게임
    if list_A.count(4) > list_B.count(4):
        print("A")
        continue


    elif list_A.count(4) > list_B.count(4) and list_A.count(3) > list_B.count(3):
        print("A")
        continue


    elif list_A.count(4) > list_B.count(4) and list_A.count(3) > list_B.count(3) > list_A.count(2) > list_B.count(2):
            print("A")
            continue

    elif list_A.count(4) > list_B.count(4) and list_A.count(3) > list_B.count(3) > list_A.count(2) > list_B.count(2) > list_A.count(1) > list_B.count(1):
            print("A")
            continue
    
    #무승부
    elif list_A.count(4) == list_B.count(4) and list_A.count(3) ==  list_B.count(3) and list_A.count(2) ==  list_B.count(2) and list_A.count(1) ==  list_B.count(1):
       print("D")
       continue


    else: print("B")
    continue



    







