'''all primes are in form of 3t+1 or 3t+2
when replacing n digit and n% 3 != 0, no doubt we get 3 number out of 10
 with sum(digits) /3 => at least 3 numbers are not prime
 => we must replace 3*i digits and cannot replace the end-digit'''
'''tổng tất cả các chữ số của số ngtố' đều có dạng 3t+1, 3t+2
khi thay n số  của số N, nếu n không chia hết cho 3 ta sẽ thu đc itts nhất 3/10 số có dạng
3t => loại vì đề bài yêu cầu 8/10 số là prime
vậy n phải chia hết cho 3. mà ta đang tìm số bế nhất nên chọn n = 3. và chữ số cuối cùng của
1 số prime chỉ là [1,3,7,9] nên không thể nằm trong số n. vậy số cần tìm cần ít nhất có dạng
bbbe (b là số thay từ 0-9, e là cs cuối). theo ví dụ số đầu tiên có 7-prime là 56003 nên ta
sẽ bắt đầu từ 5 cs: abbbe
chạy lần 1 không tìm được => tăng lên 1 cs: acbbbe trong đó a,b,c thay đổi vị trí theo tổ hợp
theo (1)
ta tìm được format thỏa mãn babcbe hoặc bcbabe thỏa mãn và có family:
babcbe = ['121313', '222323', '323333', '424343', '525353', '626363', '828383', '929393']
'''
import time
start = time.time()
import itertools
import sys
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
# (1)
cases = sorted(list(set(list(itertools.permutations(['b','b','b','a','c'])))),key=lambda x:x[0])
result = []
numbs = []
temp = []
print(cases)
for case in cases:
    for a in range(0,10):
        for c in range(0,10):
            for e in [1,3,7,9]:
                for b in range(0,10):
                    for i in case:
                        if i == 'a':
                            temp.append(str(a))
                        elif i =='b':
                            temp.append(str(b))
                        else:
                            temp.append(str(c))
                    numb = ''.join(temp) + str(e)
                    #print(numb)
                    if not numb.startswith('0') and is_prime(int(numb)):
                        numbs.append(numb)
                    temp.clear()
                #if '121313' in numbs:    
                #    print(numbs)
                if len(numbs) == 8:
                    print(numbs)
                    SystemExit()

                numbs.clear()


# babcbe = ['121313', '222323', '323333', '424343', '525353', '626363', '828383', '929393']

end = time.time()
print('times = {} s'.format(end - start))