'''có 10! cách sắp xếp 1 số từ 10 chữ số ban đầu theo thứ tự từ bé đến lớn.
ta cần tìm số thứ 1000000 tức là số cách sắp sếp thứ n = 999999.
mà 10! > n nên ta có thể thấy vị trí index 1 sẽ được chọn. 9 vị trí sau sẽ có cách sắp
xếp 9! < n. thấy n/9! xấp sỉ 2.75 tức là với số lần sắp xếp thứ n chữ số dầu tiên sẽ đến được
số 2( tính bắt đầu từ 0,1,2,..). với mỗi chữ số đầu ta có 9! cách sắp xếp . như vậy
số đầu là 2 thì ta còn n-2*9! cách xắp xếp. tương tự với các chữ số tiếp theo ta xây dựng thuật
toán'''
import time
start = time. time()
import math

t = 1000000 -1
li=[]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9,-1,-1):
    li.append(num[t//math.factorial(i)])
    num.remove(num[t//math.factorial(i)])
    t = t % math.factorial(i)
print(''.join([str(i) for i in li]))

end = time. time()
print('times = {} s'.format(end - start))