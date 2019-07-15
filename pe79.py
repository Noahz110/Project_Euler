'''làm bằng tay
hàng 1 {'8', '6', '2', '7', '3', '1'}
hàng 2 {'9', '8', '6', '2', '1', '3'}
hàng 3 {'9', '8', '6', '2', '1', '0'}
- số 7 chỉ xuất hiện ở hàng 1 => pass = 7x
- số 0 chỉ xuất hiện ở hàng 3 => pass = 7x0
- các số a=(1,2,6,8) xuất hiện ở cả 3 hàng => p = 7xax0
- số 3 không xuất hiện ở hàng cuối tức là tất cả a sẽ sau 3(vì a đều nằm ở hàng cuối)
 => p = 73ax0
- số 9 ko xuất hiện ở hàng đầu tức là tất cả a sẽ trước 9(vì hàng đầu đều có a)
=> p =73a90
- xắp xếp a ta dựa bằng mắt nhìn các cặp số trong list data thu được a = (1,6,2,8) theo đúng
thứ tự
=> p = 73162890 
'''
import time
start = time.time()

#code here
with open('p079_keylog.txt','rt') as f:
    contents = f.read()

data = list(set(contents.splitlines()))
firsts = set([i[0] for i in data])
seconds = set([i[1] for i in data])
thirds = set([i[2] for i in data])

print()

end = time.time()
print('times = {} s'.format(end - start))