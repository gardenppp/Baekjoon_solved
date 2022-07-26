T = int(input())
left_money = 0
quarter = 0
dim = 0
nickel = 0
penny = 0
for i in range(T):
    money = int(input())
    quarter = money // 25
    left_money = money - quarter*25
    dim = left_money // 10
    left_money = left_money - 10*dim
    nickel = left_money // 5
    left_money = left_money - 5*nickel
    penny = left_money
    print(quarter, dim, nickel, penny,end=' ')
    print()
    left_money = 0
    quarter = 0
    dim = 0
    nickel = 0
    penny = 0