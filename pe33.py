import time
start = time.time()

#code here
import math
total_nu, total_de = 1, 1
for nu in range(11,100):
    for de in range(nu,100):
        if (nu % 10 == 0 and de % 10 == 0) or (nu % 11 ==0 and de % 11 == 0) or (str(nu)==str(de)[::-1]) or (nu//10 == de //10):
            continue
        li_nu = [i for i in str(nu)]
        li_de = [i for i in str(de)]
        for di in li_nu:
            if di in li_de:
                li_nu.remove(di)
                li_de.remove(di)
                if nu * int(li_de[0]) == de * int(li_nu[0]):
                    total_nu *= nu
                    total_de *= de
                    # print(nu,de)
new_nu, new_de = int(total_nu / math.gcd(total_de,total_nu)), int(total_de / math.gcd(total_de,total_nu))
print(new_de)
# print(total_de,total_nu)


end = time.time()
print('times = {} s'.format(end - start))