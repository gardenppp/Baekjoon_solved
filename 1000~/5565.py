total_price = int(input())
for i in range(9):
    book_price = int(input())
    total_price -= book_price
print(total_price)