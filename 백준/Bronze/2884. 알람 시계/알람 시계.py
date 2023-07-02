h, m = map(int, input().split())
if h == 23 and m < 45:
    print(22, m + 15)
elif h == 0 and m < 45:
    print(23, m + 15)
elif h > 0 and m < 45:
    print(h - 1, m + 15)
elif m>=45:
    print(h,m-45)