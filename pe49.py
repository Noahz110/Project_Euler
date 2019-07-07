'''đề bài yêu cầu tìm 12-digits number tạo bởi 3 số 4cs thỏa mãn 3 tiêu chí như bộ 
số ban đầu.'''
import time
start = time.time()

#code here
import math
def is_prime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    elif n > 2:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
result = []
for num in range(1001,3339,2):
    if is_prime(num):
        num2 = num +3330
        num3 = num2 +3330
        if is_prime(num2) and is_prime(num3):
            digits = sorted(list(str(num)))
            digits2 = sorted(list(str(num2)))
            digits3 = sorted(list(str(num3)))
            if digits == digits2 and digits == digits3:
                result.append((num,num2,num3))
print(result)
end = time.time()
print('times = {} s'.format(end - start))