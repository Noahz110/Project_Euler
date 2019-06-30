import time
start = time.time()

#code here
import math
def nCr(n,r):
    f = math.factorial
    return f(n)//(f(r)*f(n-r))

count = 0
for n in range(1,101):
    for r in range(0,n+1):
        if nCr(n,r) > 1000000:
            count += 1
print(count)

end = time.time()
print('times = {} s'.format(end - start))