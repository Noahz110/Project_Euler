'''nof : number of fractions in form n/d as HCF(n,d)= 1
as d is a prime we get number of fracs = d-1
d is product of 2 diffirents primes a*b we get nof = (a-1)*(b-1)
d = a*b (a is prime, b = a or b is non-primes) => nof = b*(a-1)
every d can written in form d= a^a1* b^b1... as a and b are primes
=> d = N* a*b*c... (a,b,c.. are primes) so nof of (a*b*c) = (a-1)*(b-1)*(c-1)
=> nof of d = N*(a-1)*(b-1)*(c-1)
ví dụ d = 24 = 2*2*2*3 = 4*2*3 có NOF = 4*1*2 = 8
[1/24,5/24,7/24,11/24,13/24,17/24,19/24,23/24]'''
import time
start = time.time()
import math
import functools
import sys
#code here
def product_primes(d):
    primes = [] 
    i = 2
    while i*i <= d:
        if d % i:
            i += 1
        else:
            d //= i
            if i not in primes:
                primes.append(i)
    if d > 1 and d not in primes:
        primes.append(d)
    product , fractions_count = 1 , 1
    for numb in primes:
        product *= numb
        fractions_count *= (numb-1)
    return product , fractions_count

elements_count = 0 
for d in range(2,int(sys.argv[1])):
    product_d , fractions_count_d = product_primes(d)
    multi = d // product_d
    elements_count += multi * fractions_count_d
   
print(elements_count)

end = time.time()
print('times = {} s'.format(end - start))