li = list(range(1,101))
square_sum = sum(li) ** 2
sum_square = 0
for i in li:
    sum_square = sum_square + i ** 2
print(square_sum- sum_square)