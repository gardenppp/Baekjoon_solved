a,b=map(int,input().split())
if a==b and a!=0:
    print('Even',a*2)
elif a!=b:
    print('Odd',max(a,b)*2)
else :
    print("Not a moose")