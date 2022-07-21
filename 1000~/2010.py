n=int(input())
x=[]
sum=0
q=0
for i in range(n):
    a=int(input())
    x.append(a)
x.sort(reverse=True)
for i in range(n):
    sum+=x[i]
    sum-=1
print(sum+1)