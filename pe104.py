'''test if fn is last 1-9 pand (need get last 9 digits by % for faster time)
then test if fn is first 1-9 pand'''
import time
start = time.time()
import math
#code here

def is_pandigital(n):
    return sorted(n) == list('123456789')
#get first 9 digits
def first_9_digits(num):
    return num // 10 ** (int(math.log(num, 10)) - 9 + 1)
f1 = 1
f2 = 1
count = 3
while True:
    f1 , f2 = f2, f1+ f2
    if is_pandigital(str(f2%1000000000)):
        if is_pandigital(str(first_9_digits(f2))):
            break
    count += 1
print(count, f2)

end = time.time()
print('times = {} s'.format(end - start))