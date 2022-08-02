n , m , k = map(int,input().split())
cnt = 0
while n+m>=k and m>=0 and n>=0:#여자와 남자 수의 합이 k보다 클때까지는 무한반복
    n-=2
    m-=1
    cnt += 1
print(cnt-1)#마지막 경우는 k보다 클때까지이지만 k로 빠지는 경우이기 때문에 1건 제외