import time
start = time.time()

#code here
max_digits_sum = 0
for a in range(100):
    for b in range(100):
        s = a ** b
        digit_sum = sum(int(i) for i in str(s))
        if digit_sum > max_digits_sum:
            max_digits_sum = digit_sum

print(max_digits_sum)

end = time.time()
print('times = {} s'.format(end - start))