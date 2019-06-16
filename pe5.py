import math
num = 1
prime = [2,3,5,7,11,13,17,19]
non_prime = [4,6,8,9,10,12,14,15,16,18,20]
for i in prime:
    t= pow(i, int(math.log(20, i)))
    num = num * t
print(num)