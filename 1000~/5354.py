t = int(input())
for i in range(t):
    a=int(input())
    for x in range(1,a+1):
        if x==1 or x==a:
            print("#"*a)
        else:
            for y in range(1,a+1):
                if y==1 or y==a:
                    print("#",end='')
                else:   
                    print("J",end='')
            print()
    print()