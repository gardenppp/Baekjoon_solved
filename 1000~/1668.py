n = int(input())
cnt_left = 0 # 왼쪽
cnt_right = 0 # 오른쪽
tropy_list = []
max_left_tropy = 0 # 왼쪽
max_right_tropy = 0
for i in range(n):
    tropy_list.append(int(input()))
for i in tropy_list:
    if i > max_left_tropy:
        cnt_left+=1
        max_left_tropy = i
tropy_list = reversed(tropy_list)
for i in tropy_list:
    if i > max_right_tropy:
        cnt_right+=1
        max_right_tropy = i
print(cnt_left)
print(cnt_right)