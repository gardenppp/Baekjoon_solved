n = int(input())
result1 = 0
result2 = 0
result3 = 0
result4 = 0
key = 0
for i in range(n):
    a,b,c = map(int,input().split())
    if a==b and b==c:
        result1 = 10000 + a*1000
    elif a==b or a==c:
        result2 = 1000 + a*100
    elif b==c:
        result3 = 1000 + b*100
    else:
        result4 = max(a,b,c)*100
    key = max(key,result1,result2,result3,result4)
print(key)