n = int(input())
cnt = 0 # 거절당한 사람들
all_pc = [0]*101 # PC방 총 자리
custom = list(map(int,input().split()))
for i in custom:
    if all_pc[i] != 0:
        cnt+=1
    else:
        all_pc[i]=1
print(cnt)