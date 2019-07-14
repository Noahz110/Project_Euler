'''odd-digits number always had a middle digit k, so i + reversed_i always get 2k
at the middle because the inner pair cant get over 10 thus the outter pair is different
. =>counting 10**9 = 10**8'''
import time
start = time.time()

#code here
def is_odds(n):
    for i in str(n):
        if not int(i) % 2:
            return False
    return True

count = 0
list_i = [i for i in range(10**8) if i % 10]
for i in list_i:
    if is_odds(i + int(str(i)[::-1])):
        count += 1
print(count)    

end = time.time()
print('times = {} s'.format(end - start))