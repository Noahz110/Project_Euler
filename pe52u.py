'''x phai bat dau bang 1, so tiep theo < 7, so cuoi. x //3'''
import time
start = time.time()

#code here
i = 23456
while True:
    s = int('1'+str(i))
    s_list = list(str(s))
    s_list.sort()
    if set(s_list) & {'1','2','3','4','5','6'} == {'1','2','3','4','5','6'}:
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