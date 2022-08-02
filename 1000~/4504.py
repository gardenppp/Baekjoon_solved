num = int(input())
while True:
    a = int(input())
    if a==0:
        break
    elif a%num == 0:
        print("%d is a multiple of %d."%(a,num))
    else:
        print("%d is NOT a multiple of %d."%(a,num))