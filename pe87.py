'''caculate max for a,b,c
take a set as reserving results (this prevent from getting duplicated results and faster than
using list simple by us add() method)'''
import time
start = time.time()
from is_prime import is_prime
#code here
N = 50000000
def triple_num(a,b,c):
    return a**2+b**3+c**4
c_max = 84
b_max = 368
a_max = 7071
set_trip = set()
count = 0
for c in (i for i in range(c_max+1) if is_prime(i)):
    for b in (i for i in range(b_max+1) if is_prime(i)):
        if c ** 4 + b ** 3 + 2**2 >= N:
            break
        for a in (i for i in range(a_max+1) if is_prime(i)):
            t = triple_num(a,b,c)
            if t >= N:
                break
            else:
                print(t)
                set_trip.add(t)
print(len(set_trip))

end = time.time()
print('times = {} s'.format(end - start))