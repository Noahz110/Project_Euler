'''suppose n/d < 3/7 and n/d max we always get form of 3/7 - n/d = 1/7d
so n = (3d-1)/7. the greater of d the less of 1/7d we get.
we can assume that 2 notices: 1. d is as max as possible so run d from (1000000,1)
2. n is integer so 3d-1 % 7 == 0 . algorithm by Noahz'''
import time
start = time.time()
import math
from fractions import Fraction as F

#code here
max_f = 0
for d in range(1000000,1,-1):
    s = (3*d -1)
    if s % 7 == 0:
        n = int(s/7)
        max_f = F(n,d)
        break

print(max_f)

end = time.time()
print('times = {} s'.format(end - start))