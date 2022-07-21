t = int(input())
file_list = list(map(int,input().split()))
clust = int(input())
cnt = 0
for i in file_list :
    if i < clust and i != 0:
        cnt += 1
    else:
        if i % clust != 0:
            cnt += ((i//clust) +1)
        else:
            cnt += i // clust
print(clust * cnt)