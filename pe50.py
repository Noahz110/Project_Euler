import time
start = time.time()

#code here
import math
#đầu vào là giới hạn và số max_terms đã biết trước vd biết trc max_terms 1000 = 21
# đầu ra là roftop, max_prime, max_array, init_num,end_num với max_array sẽ dùng cho vòng sau
# trước hết ta tìm max prime < 10000 tiếp tục <100000 rồi cuối cùng <1000000
def find_max_consecutive_primes(roftop, count):
    def is_prime(n):
        if n == 2:
            return True
        elif n > 2:
            for i in range(2,int(math.sqrt(n))+1):
                if n % i == 0:
                    return False
            return True

    def list_primes(n):
        li = [2]
        for i in range(3,n,2):
            if is_prime(i):
                li.append(i)
        return li
    # hàm này tín giá trị khởi tạo max tức là init_num giới hạn nếu vượt quá sẽ thu được dãy có số lượng < count bất kể thế nào.
    # ta đã biết max_array = count => init_num < roftop/count
    def imax(count):
        for i in li:
            if li[i] > roftop/count:
                return i
    li = list_primes(roftop)
    max_prime , max_array = 0, 0
    for i in range(imax(count)):
        if len(li) - i < max_array:
            break
        else:
            for j in range(imax(count)+count,i,-1):
                s = sum(li[i:j])
                if s < roftop and s in li:
                    if max_array < len(li[i:j]):
                        max_prime , max_array ,init_num, end_num = s, len(li[i:j]), li[i],li[j]
                    break
    return roftop, max_prime, max_array, init_num,end_num
count10000 = find_max_consecutive_primes(10000,21)[2]
count100000 = find_max_consecutive_primes(100000,count10000)[2]
result = find_max_consecutive_primes(1000000,count100000)
print(result)
#print(max_prime, max_array,init_num,end_num)

end = time.time()
print('times = {} s'.format(end - start))