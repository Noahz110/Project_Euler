import time
start = time.time()

#code here

total = 0
digits = set('0123456789')
d6 = '5'
for d7 in set('012346789'):
    for d8 in {d8 for d8 in digits - set([d6,d7]) if int(d6+d7+d8)%11 ==0}:
        for d9 in digits - set([d6,d7,d8]):
            if int(d7 + d8 + d9) % 13 == 0:
                for d10 in digits - set([d6,d7,d8,d9]):
                    if int(d8+d9+d10) % 17 == 0:
                        for d5 in digits - set([d6,d7,d8,d9,d10]):
                            if int(d5+d6+d7) % 7 == 0:
                                for d4 in digits - set([d5,d6,d7,d8,d9,d10]):
                                    if int(d4) %2 ==0:
                                        for d3 in digits - set([d4,d5,d6,d7,d8,d9,d10]):
                                            if int(d3+d4+d5) % 3 ==0:
                                                for d2 in digits - set([d3,d4,d5,d6,d7,d8,d9,d10]):
                                                    for d1 in digits - set([d2,d3,d4,d5,d6,d7,d8,d9,d10]):
                                                        total += int(d1+d2+d3+d4+d5+d6+d7+d8+d9+d10)
                                                        print(d1+d2+d3+d4+d5+d6+d7+d8+d9+d10) 
print(total)

end = time.time()
print('times = {} s'.format(end - start))