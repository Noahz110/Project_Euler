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
                break
        return True

cnt = 1
for i in range(3,1000000,2):
    for j in range(len(str(i))):
        if not is_prime(int(''.join([str(i)[j:],str(i)[:j]]))):
            break
    else:
        cnt += 1
print(cnt)
end = time.time()
print('times = {} s'.format(end - start))