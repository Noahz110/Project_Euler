'''x phai bat dau bang 1. x chia het cho 3'''
import time
start = time.time()

#code here
i = 1
while True:
    s = int('1'+str(i))
    s_list = list(str(s))
    s_list.sort()
    if sum(int(i) for i in s_list) %3 == 0:
        li = [list(str(k*s)) for k in range(2,7)]
        for j in li:
            j.sort()
            if j != s_list:
                break
        else:
            print(s)
            break
    i += 1

end = time.time()
print('times = {} s'.format(end - start))