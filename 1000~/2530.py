h,m,s = map(int,input().split())
a=int(input())
s1=(a+s)%60
m1=(m+(a+s)//60)
m2=m1%60
h1=(h+m1//60)%24
print(h1,m2,s1)0