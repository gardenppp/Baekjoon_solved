cnt = 0
for i in range(3):
    yut_list = list(map(int,input().split()))
    for y in yut_list:
        if y == 0:
            cnt +=1    
    if cnt == 4:
        print('D')
    elif cnt == 3:
        print('C')
    elif cnt == 2:
        print('B')
    elif cnt == 1:
        print('A')
    else:
        print('E')
    cnt = 0
     