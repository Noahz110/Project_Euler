import time
start = time. time()

total = 1
for i in range(3,1003,2):
    total += 4 * i * i - 6 * (i - 1) 
print(total)

end = time. time()
print('times = {} s'.format(end - start))