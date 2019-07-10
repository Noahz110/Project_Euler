import time
start = time.time()
from fractions import Fraction as F
import functools
import math
#code here
#attempt 1 not success find the next fraction from 1/3 like pe71
""" def find_next(a,b):
    for d in range(12000,1,-1):
        s = 1+a*d
        if not s % b:
            return s//b, d
a,b = 1,3
count = 0
while F(a,b) < 1/2:
    a,b = find_next(a,b)
    count +=1 
print(count-1)"""
# attempt 2: 1/a < n/d <1/b => d/a <n < d/b:
count = 0
for d in range(2,12001):
    n = d//3 +1
    while n < d/2:
        if math.gcd(n,d) == 1:
            count +=1
        n += 1
print(count)
end = time.time()
print('times = {} s'.format(end - start))