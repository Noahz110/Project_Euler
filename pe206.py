'''square of i is 1_2_3_4_5_6_7_8_9_0 so i must end with 0
counting i from i_min = 1010101010 to i_max with stride is 10'''
import time
start = time.time()
import math
#code here
a = '1234567890'
min_i = math.floor(math.sqrt(1020304050607080900))
max_i = math.ceil(math.sqrt(1929394959697989900))
for i in range(min_i,max_i,10):
    square_i = str(i**2)
    if square_i[::2] == a:
        print(i)
        break


end = time.time()
print('times = {} s'.format(end - start))