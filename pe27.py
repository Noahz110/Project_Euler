'''notes: n=0 suy ra b is prime'''
import time
start = time. time()

import math
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
bs = [i for i in range(2,1001) if is_prime(i)]
nmax = 0
cnt = 0
for b in bs:
    for a in range(-1000,1001):
        n = 1
        while is_prime(n**2 +a*n +b):
            n+=1
        if n > nmax:
            nmax , p = n , (a,b)
print(p[0]*p[1])

end = time. time()
print('times = {} s'.format(end - start))