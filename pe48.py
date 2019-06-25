import time
start = time.time()

#code here
total = 0
for i in range(1,1001):
    total += i ** i
print(str(total)[-10:])

end = time.time()
print('times = {} s'.format(end - start))