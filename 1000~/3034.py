import math
n,w,h = map(int,input().split())
max_length = int(math.sqrt((w**2) + (h**2)))
for i in range(n):
    ans = int(input())
    if ans<=max_length:
        print("DA")
    else:
        print("NE")