'''n-digit is prime: -tổng các cs ko chia hết cho 3
-đuôi thuộc [1,3,7,9]
xét từ cao đến thấp: 7-digit ko chia hết cho 3 => a = 7 digit
abcdefg (g = [1,3,7])'''
import time
start = time.time()
import math
def is_prime(n):
    if n == 2:
        return True
    elif n > 2:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

#code here
li_digits = ['1','2','3','4','5','6','7']
for i in range(7654321,1234566,-1):
    i_digits = [j for j in str(i)]
    i_digits.sort()
    if i_digits == li_digits and str(i)[-1] in ['1','3','7'] and is_prime(i):
         print(i)
         break

end = time.time()
print('times = {} s'.format(end - start))