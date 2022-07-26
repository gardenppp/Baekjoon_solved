a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
A = 0
B = 0
cnt = 0
for i in range(10):
    if a_list[i] == b_list[i]:
        A += 1
        B += 1
    elif a_list[i] > b_list[i]:
        A += 3
        cnt = i
    else:
        B += 3
        cnt = i

if cnt == 0 and A==B:
    print(A,B)
    print("D")
else:
    if A==B:
        if max(a_list[cnt],b_list[cnt]) == a_list[cnt]:
            print(A,B)
            print("A")
        else:
            print(A,B)
            print("B")
    else:
        if max(A,B)==A:
            print(A,B)
            print("A")
        else:
            print(A,B)
            print("B")