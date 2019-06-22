import time
start = time. time()

def is_abundant(n):
    return n < sum([i for i in range(1,n) if n % i == 0])

abudants = [i for i in range(1,28123) if is_abundant(i)]
sum_two_abudant = [0]*28124
for i in range(0,len(abudants)):
    for j in range(i,len(abudants)):
        sums = abudants[i]+abudants[j]
        if sums <= 28123:
            sum_two_abudant[sums] = sums
total = 0
for x in range(1, len(sum_two_abudant)):
    if sum_two_abudant[x] == 0:
        total += x

print(total)

end = time. time()
print('times = {} s'.format(end - start))