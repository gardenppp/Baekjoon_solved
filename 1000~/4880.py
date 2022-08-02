while True:
    arr = list(map(int,input().split()))
    if arr[0]==0 and arr[2]==0:
        break
    elif arr[1]-arr[0] == arr[2]-arr[1]:
        cha = arr[1]-arr[0]
        ans = arr[2] + cha
        print("AP",ans)
    else:
        cha = arr[1]//arr[0]
        ans = arr[2]*cha
        print("GP",ans)