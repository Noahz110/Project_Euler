''' dinh nghia hàm is_pentagonal có so sánh float và int không đúng lắm
nhưng vì số vòng lặp lớn nên không dùng được cách khác để định nghĩa *hic'''
import time
start = time.time()
import math
#code here
def is_pentagonal(n):
    s = (1+math.sqrt(24*n+1))/6
    return int(s)== s

li = [int((3*h-1)*h/2) for h in range(1,10000)]
for h in li:
    for j in li:
        if is_pentagonal(h+j) and is_pentagonal(h+2*j):
            print(h,j)
            break
    else:
        continue
    break

end = time.time()
print('times = {} s'.format(end - start))