arr=list(map(int,input().split()))
arr.sort
sum1=arr[0]+arr[3]
sum2=arr[1]+arr[2]
print(abs(sum1-sum2))