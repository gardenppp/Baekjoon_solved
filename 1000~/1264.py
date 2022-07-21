moum ="aeiouAEIOU"
while True:
    sent = input()
    cnt = 0
    if sent == '#':
        break
    else:
        for i in sent:
            if i in moum:
                cnt +=1
        print(cnt)