'''cube has k-digits, cube = n**3
so other permutated cube < 10**k = kmax **3
so other permutated cube if in form i ** 3 then n < i < kmax
run i in range(n,kmax) if we find other 4 permutated cube then return cube'''
import time
start = time.time()
#code here
n = 12
while True:
    cnt = 0
    cube = n ** 3
    list_cube = sorted(str(cube))
    max_cube = 10** len(str(cube))
    for i in range(n+1, int(max_cube**(1/3))):
        if sorted(str(i**3)) == list_cube:
            cnt += 1
    if cnt == 4:
        result = cube
        break
    n += 1
print(result)
end = time.time()
print('times = {} s'.format(end - start))