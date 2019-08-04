'''x,y > n đặt x = n+ i, y = n+j biến đổi đẳng thức thu được n^2 = i*j
có n luôn viết được dưới dạng tích của các mũ số nguyên tố
 n = p1^a1 * p2^a2*... trong đó p1,p2,.. là các số nguyên tố
(vd 324 = 2^3 * 3^4)
như vậy n^2 = p1^2a1 * p2^2a2 *...
số ước của n^2 là (2a1+1)(2a2+1)....
thấy n = 2*3*5*7*11*13*17 có số nghiệm = 3*3*3*3*3*3*3 = 2187> 2000
=> xét n < 510510
'''
import time
start = time.time()
#code here
limit = 510510
list_primes = [2,3,5,7,11,13,17]
# tinh so mu cua cac thanh phan prime tao thanh n
def divisors_square(n):
    list_primes = [2,3,5,7,11,13,17]
    i = 0
    cnt = 0
    nod = 1
    while i < 7:
        if n % list_primes[i] == 0:
            n = n//list_primes[i]
            cnt += 1
        else:
            if cnt > 0:
                nod *= (2*cnt+1)
            cnt = 0
            i += 1
        if n == 1:
            nod *= (2*cnt +1)
            break
    return nod

for i in range(2, limit):
    if divisors_square(i) > 2000:
        print(i)
        break

# print(divisors_square(180180))

end = time.time()
print('times = {} s'.format(end - start))