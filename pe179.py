'''long time no see'''
import time
start = time.time()

#code here
L = 10**7
# matrix of divisors with index is n
n = [0]*(L)
# divisors
for i in range(2, L//2):
    # n chia het cho i
    for j in range(i*2, L, i):
        n[j] += 1

print(sum(n[i] == n[i - 1] for i in range(3, L)))

end = time.time()
print('times = {} s'.format(end - start))