''' 10^n - 1 > a ^ n  => a< 9'''
import time
start = time.time()

#code here
n = 1
count = 0 
while True:
    li = [i for i in range(1,10) if len(str(i**n)) == n]
    if len(li) == 0:
        break
    else:
        count += len(li)
    n += 1

print(count, n-1)
end = time.time()
print('times = {} s'.format(end - start))