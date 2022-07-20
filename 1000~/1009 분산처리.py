n=int(input())
a=[]
b=[]
for i in range(n) :
    q,w=map(int,input().split())
    a.append(q)
    b.append(w)

for i in range(n) :
    x=a[i]%10
    if x==0:
        print(10)
    elif x in [1,5,6] :
        print(x)
    elif x in [4,9] :
        if b[i]%2==0 :
            print(x**2%10)
        else : 
            print(x)
    else :
        if b[i]%4==0 :
            print(x**4%10)
        else :
            print(x**(b[i]%4)%10)