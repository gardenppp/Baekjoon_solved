temp = float(input())
while True:
    a = float(input())
    if a==999:
        break
    else:
        cha = a-temp
        print("%.2f"%cha)
        temp = a