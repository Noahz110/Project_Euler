t = int(input("Nhap vao so mu: "))
sum_digit = 0
power = str(2 ** t)
for i in power:
    sum_digit += int(i)
print(sum_digit)