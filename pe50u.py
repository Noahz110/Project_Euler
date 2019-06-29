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

def list_primes(n):
    li = [2]
    for i in range(3,n,2):
        if is_prime(i):
            li.append(i)
    return li

li = list_primes(1000)
max_prime , max_array = 0, 0
for i in range(len(li)):
    if len(li) - i < max_array:
        break
    else:
        for j in range(i+2,len(li)):
            s = sum(li[i:j])
            while s < 1000 and s in li:
                if max_array < len(li[i:j]):
                    max_prime , max_array = s, len(li[i:j])
            break

print(max_prime)

end = time.time()
print('times = {} s'.format(end - start))