a=int(input()) # 150
b=int(input()) # 266
c=int(input()) # 427
x = str(a*b*c) # 17037300
cnt = 0
for i in range(10): # 0~9 까지
    for j in x: 
        if i == int(j): # x값 각 자리가 i랑 맞는지 비교
            cnt += 1 
    print(cnt)
    cnt = 0