t = int(input())
for i in range(t):
    a,b = input().split()
    a = int(a)
    print(b[:a-1] + b[a:])