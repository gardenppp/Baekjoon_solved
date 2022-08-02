n,w,h,l=map(int,input().split())
s=(w//l)*(h//l)
if n>s :
    print(s)
else :
    print(n)