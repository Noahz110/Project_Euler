import math
num = 600851475143
max_factor = 0
dec = 1
for i in range(2,int(math.sqrt(num))):
    if num % i == 0:
        for x in range(2,int(math.sqrt(i))):
            if i % x == 0:
                dec = 0
        if dec == 1:
            max_factor = i
print(max_factor)


