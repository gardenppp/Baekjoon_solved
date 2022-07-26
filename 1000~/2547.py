import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    bincan = input()
    student_num = int(input())
    sum = 0
    for y in range(student_num):
        sum += int(input())
    if sum % student_num == 0:
        print("YES")
    else:
        print("NO")