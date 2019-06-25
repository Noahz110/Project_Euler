'''9! * n luôn > A. mà 9! * 7 = 2540160 < 9999999
suy ra số chữ số n <= 7'''
import time
start = time.time()

#code here
import math
total = 0
for a in range(3,9999999):
    if a == sum([math.factorial(int(i)) for i in str(a)]):
        total += a
print(total)

end = time.time()
print('times = {} s'.format(end - start))