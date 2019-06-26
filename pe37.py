import time
start = time.time()

#code here
basic_primes = [2, 3, 5, 7]
import math
def is_prime(n):
    if n == 2:
        return True
    elif n > 2:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True 
count = 0
total = 0
number = 11
while count != 11:
    n = len(str(number))
    if str(number)[-1] in ['3','7'] and str(number)[0] in ['2','3','5','7'] and is_prime(number):
        li = [(number // pow(10, i), number % pow(10, i)) for i in range(1,n)]
        for right , left in li:
            if not is_prime(right) or not is_prime(left):
                break
        else:
            print(number)
            total += number
            count += 1
    number += 2 
print(total)
# primes_under_100 = [i for i in range(11,100) if is_prime(i) and i% 10 in [3,7] and i//10 in [1,3,7,9]]
# print(primes_under_100)

end = time.time()
print('times = {} s'.format(end - start))