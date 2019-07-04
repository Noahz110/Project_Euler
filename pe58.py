import time
start = time.time()

#code here
import math
from fractions import Fraction as F
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n > 2:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

diagonals = [1]
i = 3
count = 0
while True:
    temp = [diagonals[-1]+(i-1)*j for j in range(1,5)]
    diagonals.clear()
    diagonals.append(temp[-1])
    for j in temp:
        if is_prime(j):
            count += 1
    if F(count, 2*i-1) < F(10,100):
        print(i)
        print(count, 2*i-1)
        break
    i += 2

end = time.time()
print('times = {} s'.format(end - start))