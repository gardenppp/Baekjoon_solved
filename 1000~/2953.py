score_list = []
for i in range(5):
    score_list.append(sum(map(int,input().split())))
print(score_list.index(max(score_list)) + 1, max(score_list),end=' ')