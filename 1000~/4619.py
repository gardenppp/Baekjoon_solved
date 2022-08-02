while True:
    b,n = map(int,input().split())
    if b==n==0:
        break
    else:
        i = 0 # A 값
        while i**n < b:
            i += 1 # i값의 n제곱이 b값을 이미 넘어섬
        if (i**n)-b < b-((i-1)**n):
            print(i)
        else:
            print(i-1)