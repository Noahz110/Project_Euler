'''F(n,k) = F(n,k-1) + F(n-k,k)
trong đó F(n,k) là số cách viết n dưới dạng tổng các số < k'''
import time
start = time.time()
import math
#code here
n = 100
m = [0] * 101
m[0] = 1
for i in range(1,100):
    for j in range(i,101):
        m[j] += m[j-i]

print(m[100])


# print(result)

end = time.time()
print('times = {} s'.format(end - start))