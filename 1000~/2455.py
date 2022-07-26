sum1=0
result=0
for i in range(4):
    a,b=map(int,input().split())
    sum1=sum1-a+b
    if sum1>=result:    
        result = sum1
print(result)