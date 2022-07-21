from math import*
case_num=int(input())
for i in range(case_num):
    n,m=map(int,input().split())
    bridge = factorial(m)// (factorial(m-n)*factorial(n))
    print(bridge)