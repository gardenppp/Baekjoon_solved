a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
x=int(b//d)
y=int(c//e)

if x>=y :
    if b%d==0 :
        print(a-x)
    else :
        print(a-x-1)
else :
    if c%e==0 :
        print(a-y)
    else :
        print(a-y-1)