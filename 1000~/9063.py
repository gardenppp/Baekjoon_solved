t = int(input())
list_x = []
list_y = []
for i in range(t):
    x,y=map(int,input().split())
    list_x.append(x)
    list_y.append(y)
garo = max(list_x)-min(list_x)
sero = max(list_y)-min(list_y)
print(garo*sero)