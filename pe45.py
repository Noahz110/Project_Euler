import time
start = time.time()
import math
#code here
def is_pentagonal(n):
    s = (1+math.sqrt(24*n+1))/6
    return int(s)== s

def is_hexagonal(n):
    s = (1+math.sqrt(8*n+1))/4
    return int(s) == s
i = 286
while True:
    T = int(i*(i+1)/2)
    if is_hexagonal(T) and is_pentagonal(T):
        print(T)
        break
    i += 1


end = time.time()
print('times = {} s'.format(end - start))