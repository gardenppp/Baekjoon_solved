n=int(input())
q=5
w=7
for i in range(1,n):
    q+=w
    w+=3
print(q%45678)