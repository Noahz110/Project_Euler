import math
def num_divisors(n):
    num_factors  = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            num_factors += 2
            if n == i * i:
                num_factors -= 1
    return num_factors

for i in range(1,1000000):
    result = int(i*(i+1)/2)
    if num_divisors(result) > 500:
        print(result) 
        break    