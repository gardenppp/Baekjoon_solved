while True:
    a = int(input()) # 받아서 리스트형태로 각 자리를 찢기 위해 int 형으로 받음 ex) 673
    if a == 0: # 0 입력시 종료
        break
    while a>9: # 각 자리 합이 2자리수가 되면 종료
        a = sum(map(int,list(str(a)))) # 각 자리를 스트링 변환 후 리스트 에 담는다 (map함수 이용) ex) ['6','7','3']
    print(a) 