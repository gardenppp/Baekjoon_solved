x, y = map(int,input().split())
seven_price = x * 1000/y
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    seven_price = min(seven_price,(a*1000/b))
print(round(seven_price,2))