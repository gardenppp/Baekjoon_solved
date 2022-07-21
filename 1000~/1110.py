num = int(input()) 
key = num
cnt=0
while True:
    a = num//10 
    b = num % 10 
    num = (a + b) % 10 
    num = b*10 + num 
    cnt += 1
    if key == num:
        break
print(cnt)