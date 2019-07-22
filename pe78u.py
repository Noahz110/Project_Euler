'''from pe76 but takes many times, maybe need different algorithm'''
import time
start = time.time()
import math
#code here
def p(n):
    m = [0] * (n+1)
    m[0] = 1
    for i in range(1,n):
        for j in range(i,n+1):
            m[j] += m[j-i]

    return m[n] + 1
n = 1
while True:
    if not p(n) % 1000000:
        result = (n , p(n))
        break
    n += 1

print(result)

end = time.time()
print('times = {} s'.format(end - start))