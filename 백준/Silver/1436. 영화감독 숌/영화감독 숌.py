n = int(input()) #n번째 영화
i = 0
count = 0
while True:
    i+=1
    if '666' in str(i):# str(i) = 666
        count += 1 #순서
        if n == count: #1편의
            print(str(i)) #제목은 지구종말 666이에요
            break
