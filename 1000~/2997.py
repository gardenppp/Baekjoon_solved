a = list(map(int,input().split()))
a.sort()
if a[1]-a[0] == a[2]-a[1]:
    print(a[0] + (a[1]-a[0])*3)
elif a[1]-a[0] < a[2]-a[1]:
    print(a[1] + (a[1]-a[0]))
else:
    print(a[0] + (a[2]-a[1]))