''' tìm số max ratio trong 1 khoảng n. tức là phi(i) càng nhỏ càng tốt
nhận thấy mỗi số tự nhiên đếu là tích của các số nguyên tố.
=>i = tích các số nguyên tố  khác nhau. như vậy i sẽ có ít nhất 1 UCLN với 1 số < nó
vd: i =2*3*5*7 =210. tất cả các số < 210 đều chia hết cho 2 or 3 or 5 or 7 trừ các số nguyên tố
như vậy phi(i) =[1,các số nguyên tố <i] là ít nhất
như vậy muốn tìm i trong khoảng n chỉ cần i có dạng 2*3*5*7*... thỏa mãn i < n'''
import time
start = time.time()

#code here
import math
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
def find_max_ratio(n):
    result = 2
    for i in range(3,n,2):
        if is_prime(i):
            if result * i < n:
                result *=i
            else:
                break
    return result
print(find_max_ratio(1000000))
end = time.time()
print('times = {} s'.format(end - start))