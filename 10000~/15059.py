a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
sum=0
if a2>a1:
    sum=a2-a1
if b2>b1:
    sum+=b2-b1
if c2>c1:
    sum+=c2-c1
print(abs(sum))