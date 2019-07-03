import time
start = time.time()

#code here
from fractions import Fraction as F
''' # ok but get exception limit Recursion:
def expansion(n):
    if n == 1:
        return F(1,2)
    else:
        return F(1,2+expansion(n-1))
count = 0
for i in range(1,1000):
    result = 1 + expansion(i)
    if len(str(result.numerator)) > len(str(result.denominator)):
        count += 1
print(count)
'''
#try another algorithm
'''we can see n(k+1)/d(k+1) = 1 + 1/(1+nk/dk) = nk+2dk / nk+ dk'''
n , d = 1 , 1
count = 0
for i in range(1,1001):
    n , d = n +2*d , n+ d
    if len(str(n+2*d)) > len(str(n+d)):
        count += 1
print(count)
end = time.time()
print('times = {} s'.format(end - start))