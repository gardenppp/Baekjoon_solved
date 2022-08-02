a,b,c,d = map(int,input().split())
people_list = list(map(int,input().split())) # 사람들을 리스트로 입력받아서 for 문 안에서 사람별로 계산하게 하기
for i in people_list:
    cnt = 0 # 공격받은 횟수, 사람별로 초기화해야 하므로 for문 안에서 선언
    if 0< i%(a+b) <= a: # 공격시간과 휴식시간의 합으로 나눈 나머지가 공격시간보다 작거나 같으면 공격 받은 것이므로 횟수 추가
        cnt+=1
    if 0< i%(c+d) <= c:
        cnt+=1
    print(cnt)