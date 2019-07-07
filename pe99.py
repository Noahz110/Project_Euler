'''a^b = 2^(x*b) trong đó 2^x = a => đưa mọi số về dạng 2^t rồi so sánh t với nhau'''
import time
start = time.time()

#code here
import math
with open('p099_base_exp.txt','rt') as f:
    contents = f.read()
temp = contents.strip().split('\n')
index_pairs = [tuple(i.strip().split(',')) for i in temp]
list_exp = []
for base, exponent in index_pairs:
    list_exp.append(int(exponent) * math.log(int(base),2))
    print(list_exp[-1])
t = max(list_exp)
print(list_exp.index(t)+1)

end = time.time()
print('times = {} s'.format(end - start))