lst =[]# 난쟁이 담을 리스트
end_loop = True
for _ in range(9):
    K = int(input())
    lst.append(K)

for i in range(len(lst)-1): #0~7까지
    
    for j in range(i, len(lst)-1): #0~7까지
        
        a = lst.pop(i)
        b = lst.pop(j)

        if sum(lst) == 100:
            lst.sort()
            for z in lst:
                print(z)
            
            end_loop = False
            break

        else:

            lst.insert(i,a)
            lst.insert(j+1,b)

    if end_loop == False:
        break

    



    