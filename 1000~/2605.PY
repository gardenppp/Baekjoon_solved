# insert(인덱스, 값) 함수를 사용함 
n = int(input()) # 5
student_list = list(map(int,input().split())) # [0 1 1 3 2]
ans_list = []
for i in range(n):
    ans_list.insert(i-student_list[i],i+1)
for x in ans_list:
    print(x,end=' ')