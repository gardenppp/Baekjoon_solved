b1,b2=map(int,input().split())
d1,d2=map(int,input().split())
j1,j2=map(int,input().split())
if abs(j1-d1)+abs(j2-d2)>max(abs(j1-b1),abs(j2-b2)):
    print('bessie')
if abs(j1-d1)+abs(j2-d2)<max(abs(j1-b1),abs(j2-b2)):
    print('daisy')
if abs(j1-d1)+abs(j2-d2)==max(abs(j1-b1),abs(j2-b2)):
    print('tie')