import time
start = time. time()

def is_abundant(n):
    return n < sum([i for i in range(1,n) if n % i == 0])
'''
def is_sum_two_abudant(n):
    for i in range(1,n):
        if is_abundant(i) and is_abundant(n-i):
            return True
            break
    else:
        return False
'''
abudants = [i for i in range(1,28123) if is_abundant(i)]
sum_two_abudant = list(range(1,28124))
for i in range(0,len(abudants)):
    for j in range(i,len(abudants)):
        sums = abudants[i]+abudants[j]
        if sums <= 28123 and sums in sum_two_abudant:
            sum_two_abudant.remove(sums)
result = sum(sum_two_abudant)
#result = sum([i for i in range(1,28123) if not is_sum_two_abudant(i)])
print(result)

end = time. time()
print('times = {} s'.format(end - start))