a,b,c=map(int,input().split())
sum1=a*b/c
sum2=a/b*c
print(int(max(sum1,sum2)))