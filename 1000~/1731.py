import sys
input = sys.stdin.readline
t = int(input())
num_list = []
for i in range(t):
    num_list.append(int(input()))
if num_list[1]-num_list[0] == num_list[2]-num_list[1]:
    rate = num_list[1]-num_list[0]
    print(rate + num_list[t-1])
else:
    rate = num_list[1] // num_list[0]
    print(rate * num_list[t-1])