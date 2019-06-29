import time
start = time.time()

#code here
import math
def is_prime(n):
    if n == 2:
        return True
    elif n > 2:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
# list prime < n
def list_primes(n):
    li = [2]
    for i in range(3,n,2):
        if is_prime(i):
            li.append(i)
    return li

def is_result(n):
    if is_prime(n):
        return False
    else:
        for i in list_primes(n):
            s = math.sqrt((n - i) /2)
            if int(s) == s:
                return False
        return True


n = 9
while True:
    if is_result(n):
        print(n)
        break
    n +=2


end = time.time()
print('times = {} s'.format(end - start))