import time
start = time.time()
from math import factorial as f

#code here
def factorial_digits(n):
    return sum(f(int(i)) for i in str(n))

count = 0
for num in range(1,1000000):
    chains = [num]
    while True:
        temp = factorial_digits(chains[-1])
        if temp not in chains:
            chains.append(temp)
        else:
            break
    if len(chains) == 60:
        count += 1
print(count)

end = time.time()
print('times = {} s'.format(end - start))