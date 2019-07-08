'''all primes are in form of 3t+1 or 3t+2
when replacing n digit and n% 3 != 0, no doubt we get 3 number out of 10
 with sum(digits) /3 => at least 3 numbers are not prime
 => we must replace 3*i digits and cannot replace the end-digit'''
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
list_primes = [i for i in range(100000) if is_prime(i) and i > 10000]
cases = sorted(list(set(list(itertools.permutations(['b','b','b','a','c'])))),key=lambda x:x[0])
result = []
numbs = []
temp = []
for case in cases:
    for a in range(0,10):
        for c in range(0,10):
            for e in [1,3,7,9]:
                for b in range(0,10):
                    for i in case:
                        if i == 'a':
                            temp.append(str(a))
                        elif i =='b':
                            temp.append(str(b))
                        else:
                            temp.append(str(c))
                        numb = ''.join(temp) + str(e)
                        if not numb.startswith('0') and is_prime(int(numb)):
                            numbs.append(numb)
                if len(numbs) == 8:
                    result.append(numbs)
                numbs.clear()
                temp.clear()

print(result)

end = time.time()
print('times = {} s'.format(end - start))