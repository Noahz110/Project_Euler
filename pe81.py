'''ĐI từ góc dưới lên. các điểm ở biên phải và dưới sẽ chỉ có 1 đường.
xét 1 điểm Mij không ở biên. ta sẽ có 2 th nối với ô ở dưới Mi+1,j hoặc bên phải Mi,j+1
. ta chỉ việc so sánh 2 tổng rồi chọn tổng bé hơn. điều này đúng nếu bắt đẩu đi từ điểm góc
dưới bên phải cộng dồn lên.xet điểm x các điểm trước nó (c,d) trong đó c = c + min(a,b), d =d + min(e,f)
vì vậy x sẽ đạt min khi cộng. thuật toán -> điểm trên đỉnh chính là tổng min. Nx giống bài 18 và 67 '''
import time
start = time.time()

#code here

with open('p081_matrix.txt','rt') as f:
    data = f.readlines()
M = [[int(j) for j in i.strip().split(',')] for i in data]
# tính các giá trị biên phải và dưới vì chỉ có 1 
for i in range(78,-1,-1):
    M[79][i] += M[79][i + 1]
    M[i][79] += M[i + 1][79]
#update các điểm còn lại M[i][j] với 2 điểm phải và dưới(so sánh lấy min 1 trong 2)
for i in range(78,-1,-1):
    for j in range(78,-1,-1):
        M[i][j] += min(M[i+1][j], M[i][j+1])

print(M[0][0])


end = time.time()
print('times = {} s'.format(end - start))