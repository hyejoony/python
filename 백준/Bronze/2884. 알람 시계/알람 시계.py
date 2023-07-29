h , m = map(int,input().split())
if 0 <h < 24 and m<45:
    print(h-1,m+15)
elif h ==0 and m<45:
    print(23,m+15)
# elif 0 < h < 24 and m >=45:
#     print(h, m-45)
else:
    print(h, m-45)