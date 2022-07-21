from sys import*
m,l = stdin.readline().split()
for i in range(2,int(l)):
    if int(m)%i==0:
        print("BAD",i)
        exit()
print("GOOD")