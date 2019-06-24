import time
start = time.time()
import math
li = []
for a in range(2,101):
    for b in range(2,101):
        n = pow(a, b)
        if n not in li:
            li.append(n)
print(len(li)) 

end = time.time()
print('times = {} s'.format(end - start))