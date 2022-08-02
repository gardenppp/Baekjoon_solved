y1,m1,d1=map(int,input().split())
y2,m2,d2=map(int,input().split())
e=y2-y1#연 나이
w=y2-y1+1#세는 나이
if m2>m1 :
    q=y2-y1# 만 나이
else :
    if m2==m1 and d2>=d1:
        q=y2-y1
    else :
        q=y2-y1-1
print(q)
print(w)
print(e)