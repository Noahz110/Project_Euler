import time
start = time.time()

#code here
frac = ''
i = 1
prod = 1
while len(frac) <= 1000000:
    frac += str(i)
    i += 1
prod = int(frac[0]) * int(frac[9]) * int(frac[99]) * int(frac[999]) * int(frac[9999])* int(frac[99999]) * int(frac[999999])
print(prod)


end = time.time()
print('times = {} s'.format(end - start))