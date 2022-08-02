import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    nums = list(map(int,input().split()))
    sum = 0
    jjaksu = []
    for x in nums:
        if x % 2==0:
            sum += x
            jjaksu.append(x)
    print(sum, min(jjaksu))