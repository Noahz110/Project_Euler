import time
start = time.time()

#code here
total = 0
for i in range(1,1000000):
    if str(i) == str(i)[::-1]:
        if bin(i)[2:] == bin(i)[:1:-1]:
            total += i
print(total)

end = time.time()
print('times = {} s'.format(end - start))