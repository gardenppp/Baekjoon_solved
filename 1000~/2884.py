hour, minute = map(int,input().split())
if minute-45 < 0:
    if hour==0:
        hour = 23
        minute = minute + 60 - 45
    else:
        hour-=1
        minute = minute + 60 - 45
else:
    minute = minute - 45
print(hour,minute)