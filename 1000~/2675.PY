num = int(input())
sum=''
for i in range(num):
    n,word = map(str,input().split())
    n=int(n)
    for y in word:
        sum+=y*n
    print(sum)
    sum=''