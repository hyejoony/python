x = int(input()) #주어진 수 ex 26

if x <10 : #0
    str_x= '0'+str(x)  #'01'
if x >=10:
    str_x = str(x) #'10'

count = 0
while True:
    new_int = int(str_x[0]) + int(str_x[1]) # 2+6 = 8
    new_str = str(int(str_x[1])) + str(new_int)[-1] #'6'+'8' ='68'
    count += 1
    if x == int(new_str):
        break
    str_x = new_str
print(count)
