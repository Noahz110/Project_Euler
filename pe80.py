'''it need long lines explain so i will point u a link 
how to caculate sqrt(n) in i digits here:
https://math.stackexchange.com/questions/916190/calculate-more-digits-of-square-root-of-2/916263#916263'''
# or can show sqrt(2) with decimal package https://docs.python.org/3/library/decimal.html
import time
start = time.time()
import math
#code here
irrationals = (i for i in range(101) if math.sqrt(i) != int(math.sqrt(i)))
def digital_sum(n):
    a = int(math.sqrt(n))
    remain = n - a*a
    for i in range(99):
        temp = int(str(remain) + '00')
        core = a * 2
        for j in range(9,-1,-1):
            prod = int(str(core) + str(j)) * j
            if prod < temp:
                a = a*10 + j
                remain = temp - prod
                break
    return sum(int(k) for k in str(a))

total = 0
for num in irrationals:
    total += digital_sum(num)
print(total)

# print(digital_sum(5))      


end = time.time()
print('times = {} s'.format(end - start))