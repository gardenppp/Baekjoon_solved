a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())
x=0
y=0
if a1==a2:
    x=a3
elif a2==a3:
    x=a1
else:
    x=a2
if b1==b2:
    y=b3
elif b2==b3:
    y=b1
else:
    y=b2
print(x,y,end=' ')