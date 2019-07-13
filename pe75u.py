import time
start = time.time()

#code here
count = 0
for L in range(12,1500):
    inner_count = 0
    for a in range(L//3):
        for c in range(L//3 + 1,L):
            if a**2 + (L-a-c)**2 == c**2:
                inner_count += 1
    if inner_count == 1:
        count += 1
print(count)

end = time.time()
print('times = {} s'.format(end - start))