import time
start = time.time()
import math
from is_prime import is_prime
#code here
def is_square(n):
    return math.sqrt(n) == int(math.sqrt(n))

list_D = [i for i in range(2,100) if not is_square(i)]
max_x, max_D = 0,0
for D in list_D:
    y = 1
    while True:
        x = 1 + D * pow(y,2)
        if is_square(x):
            break
        y += 1
    if max_x < int(math.sqrt(x)):
        max_x, max_D, max_y = int(math.sqrt(x)), D , y
print(max_x, max_D, max_y)


end = time.time()
print('times = {} s'.format(end - start))