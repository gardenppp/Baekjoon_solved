n = int(input())
print_num = 0
for i in range(1,n+1):
    div_num = list(map(int,str(i)))
    sum_num = i+ sum(div_num)
    if sum_num == n:
        print_num = i
        break
print(print_num)