import time
start = time.time()

#code here
# số nhân phải bắt đầu bằng đầu 9
range_num = [i for i in range(1,98746) if str(i).startswith('9')] # so be nhat va lon nhat co the nhan
range_list = list(range(1,10))
def is_pandigital(n):
    if len(n) != 9:
        return False
    else:
        li = [i for i in n]
        li.sort()
        if li == ['1','2','3','4','5','6','7','8','9']:
            return True
        else:
            return False

max_pandi = 0
for num in range_num:
    i = 1
    partitions = ''
    while len(partitions) < 9:
        partitions += str(num * i)
        i += 1
    if is_pandigital(partitions):
        if max_pandi < int(partitions):
            max_pandi = int(partitions)

print(max_pandi)



end = time.time()
print('times = {} s'.format(end - start))