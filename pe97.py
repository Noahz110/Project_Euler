import time
start = time.time()

#code here
a = (28433*pow(2,7830457)+1) % (10**10)
print(a)

end = time.time()
print('times = {} s'.format(end - start))