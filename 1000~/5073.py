while True:
    arr = list(map(int,input().split()))
    arr.sort()
    if arr[0] == 0:
        break
    elif arr[0] + arr[1] <= arr[2]:
        print("Invalid")
    elif max(arr) == min(arr):
        print("Equilateral")
    elif arr[0] == arr[1] or arr[1] ==arr[2] or arr[0] == arr[2]:
        print("Isosceles")
    else:
        print("Scalene")