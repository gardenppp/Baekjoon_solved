n,L,d = map(int,input().split()) # 2 5 7
all_track = [False] * (n*L + (n-1)*5) # 매초를 False값으로 자리를 만듬 즉 True로 만들어질 칸은 노래중.
for i in range(n):
    x = (L+5) * i # 노래 한곡 + 쉬는 시간 (한 트랙)
    for j in range(x,x+L):
        all_track[j] = True # 노래 중인 시간을 True값으로 바꿔줌
ans = 0
while ans < len(all_track): # all_track 보다 ans의 값이 커지면 그게 답이므로 조건선정
    if not all_track[ans]:
        break
    ans += d # True 값이 아니므로 d 만큼 증가시킴
print(ans)