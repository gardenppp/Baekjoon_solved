cnt = 0
while True:
    a,b =map(int,input().split())
    cnt+=1
    if a==b==0:
        exit()
    else:
        die = False
        while True:
            x,y = input().split()
            y=int(y)
            if x=='#' and y==0:
                break
            if not die:
                if x=='E':
                    b-=y
                elif x=='F':
                    b+=y
                if b<=0:
                    die = True
        if b<=0 :
            print(cnt, "RIP")
        elif a//2 < b and b<a*2:
            print(cnt,":-)")
        else:
            print(cnt,":-(")