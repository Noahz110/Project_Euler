import time
start = time.time()
from fractions import Fraction as F
#code here
def is_bouncy(n):
    sort_n = ''.join(sorted(str(n)))
    if sort_n != str(n) and sort_n[::-1] != str(n):
        return True
    return False
count = 0
for i in range(1,1000000000):
    if is_bouncy(i):
        count += 1
    if F(count,i) == F(99,100):
        break
print(count,i)
end = time.time()
print('times = {} s'.format(end - start))