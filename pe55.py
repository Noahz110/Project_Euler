import time
start = time.time()

#code here
def is_panlindromic(n):
    return str(n) == str(n)[::-1]

def is_lychrel(n):
    for i in range(1,50):
        n = n+ int(str(n)[::-1])
        if is_panlindromic(n):
            return False
    return True

count = 0
for i in range(1,10000):
    if is_lychrel(i):
        count +=1
print(count)


end = time.time()
print('times = {} s'.format(end - start))