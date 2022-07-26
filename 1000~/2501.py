num , key_num = map(int,input().split())
yak_list = []
for i in range(1,num+1):
    if num % i ==0:
        yak_list.append(i)
yak_list.sort()
if len(yak_list) < key_num:
    print(0)
else:
    print(yak_list[key_num-1])