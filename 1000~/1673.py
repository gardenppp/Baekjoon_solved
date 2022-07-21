import sys
input = sys.stdin.readline
try : 
    while True:
        n,k = map(int,input().split()) # 10 3
        chicken = n + (n//k) # 쿠폰을 전부 사용할 때 추가로 받는 쿠폰을 제외한 기본 총 치킨 갯수 [13]
        while n >= k: # 도장갯수가 k 보다 작을때까지 (여기 반복문에서는 n을 쿠폰이 아닌 도장갯수로 봄)
            n = (n//k) + (n%k) # 현재 가지고 있는 도장은 13마리를 먹고 받는 4장과 남은 1장 
            chicken += n//k # 그래서 총 먹는 치킨은 13마리와 도장을 3개당 1마리로 바꾼 값의 총합
        print(chicken)
except :
    exit()