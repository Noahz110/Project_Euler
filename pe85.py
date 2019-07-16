'''giả sử ma trận m x n số loại hình chữ nhật con(không trùng nhau về kích thước)
là m*n hình. gs 1 loại hình con có trong hình mẹ là ixj 
thì trong hình ban đầu sẽ có (m-i+1)*(n-i+1) hình ixj. (đơn giản là ta trượt hình ixj
trong hình mẹ. lại có i=range(1,m), j=range(1,n) suy ra tổng các hình con có trong mxn
A = m*n*(m+1)*(n+1)/4. (tự biến đổi) để A gần 2tr nhất thì tìm gtri m,n sao cho A - 2tr min
biết m*n < 2828 (tự hiểu)'''
import time
start = time.time()
import math
#code here
mse = 8000000
for m in range(2,2828):
    for n in range(2,2828):
        numb_rectangles = m*n*(m+1)*(n+1)
        err = 8000000 - numb_rectangles
        if err < 0:
            continue
        if mse > err:
            mse , m_result, n_result = err, m, n
print(mse, m_result, n_result)
print(m_result * n_result)
end = time.time()
print('times = {} s'.format(end - start))
# 36x77