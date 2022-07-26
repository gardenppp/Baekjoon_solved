n = int(input())
sum = 0
cnt = 0
ans_list = list(map(int,input().split()))
for i in ans_list:
    if i==1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)