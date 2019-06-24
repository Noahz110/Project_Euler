'''đầu tiên ta nhân 1 với 10. tìm phần dư của 10/d là re. tiếp tục lấy re*10/d rồi lại lấy
phần dư re2..... nếu phần dư = 0 ta có thể kết luận số này ko vô hạn. nếu ta phát hiện re[n] 
nhận được có trùng với re[m] của các phép chia trước thì vòng lặp từ m->n chính là số chữ số
lặp cần tìm. ta chạy d từ 1-1000 tìm d có max m-n sẽ là d cần tìm'''
import time
start = time.time()
import math
remain = []
cnt = 0
max = 0
for d in range(2,1000):
    remain.append(10 % d)
    while remain[-1] != 0:
        re = 10 * remain[-1] % d
        if re not in remain:
            remain.append(re)
        else:
            cnt = len(remain[remain.index(re):])
            break
    if cnt > max:
        max , result = cnt , d
    remain.clear()
print(result)
end = time.time()
print('times = {} s'.format(end - start))