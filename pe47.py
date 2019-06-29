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
# tra ve so prime factors cua n
def list_prime_factors(n):
    li = []
    while n % 2 == 0:
        li.append(2)
        n /= 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            li.append(i)
            n /= i
    if n > 2:
        li.append(int(n))
    return len(set(li))
    
n = 210
while True:
    if list_prime_factors(n) == 4:
        if list_prime_factors(n+1) == 4:
            if list_prime_factors(n+2) == 4:
                if list_prime_factors(n+3) == 4:
                    print(n)
                    break
    n +=1
end = time.time()
print('times = {} s'.format(end - start))