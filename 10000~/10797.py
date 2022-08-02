a=int(input())
car=list(map(int,input().split()))
n=0
for i in car :
    if a==i:
        n+=1
print(n)