a,b,c=map(int,input().split())
q=11*24*60+11*60+11
w=a*24*60+b*60+c
z=w-q
if z<0 :
    print(-1)
else :
    print(z)