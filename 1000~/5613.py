a = int(input())
while True:
    b = input()
    if b == '=':
        break
    n=int(input())
    if b == '+':
      a += n
    elif b == '-':
        a -= n
    elif b == '*':
        a = a * n
    elif b == '/':
        a = a//n
print(a)