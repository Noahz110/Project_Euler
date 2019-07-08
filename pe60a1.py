import time
start = time.time()
import itertools
#code here
import math
def is_prime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    elif n > 2:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
list_primes = [str(i) for i in range(1000) if is_prime(i)]
result = []
for a in list_primes:
    for b in list_primes:
        for c in list_primes:
            for d in list_primes:
                list_pairs = [''.join(i) for i in list(itertools.permutations([a,b,c,d],2))]
                for pair in list_pairs:
                    if not is_prime(int(pair)):
                        break
                else:
                    result.append([a,b,c,d])
print(result)


end = time.time()
print('times = {} s'.format(end - start))