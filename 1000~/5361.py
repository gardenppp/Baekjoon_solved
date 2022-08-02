blaster = 350.34
look_sensor = 230.90
hear_sensor = 190.55
arm = 125.30
leg = 180.90
T = int(input())
for i in range(T):
    a,b,c,d,e = map(int,input().split())
    sum = a*blaster + look_sensor*b + hear_sensor*c + arm*d + leg*e
    sum = round(sum,2)
    print("$%.2f"%sum)