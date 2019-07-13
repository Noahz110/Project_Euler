import time
start = time.time()
from fractions import Fraction as F
#code here
e = [2]
i = 1
while len(e) < 100:
    e.extend([1,2*i,1])
    i += 1
num_100 = e[99]
for a in e[98::-1]:
    num_100 = a + F(1,num_100)
numer = list(str(num_100.numerator))
result = sum(int(j) for j in numer)
print(result)
end = time.time()
print('times = {} s'.format(end - start))