# (0,1),(0,2),(1,1),(1,2),(2,2) 이 패턴을 보면 2중for문이 생각난다.
n = int(input())
sum = 0
for i in range(0,n+1):
    for y in range(i,n+1):
        sum += i+y
print(sum)