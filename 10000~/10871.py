bum , key = map(int,input().split())
sum_list = list(map(int,input().split()))
for i in range(bum):
    if sum_list[i] < key:
        print(sum_list[i],end=' ')