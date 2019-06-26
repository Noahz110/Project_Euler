    '''My algorithm: Số cách đến 1 điểm sẽ bằng tổng số cách đến của 2 điểm
    trước nó. Số cách đến tại các điểm biên trái và trên sẽ chỉ = 1.
    Đặt ma trận điểm điến là S.
    như vậy S[0][i]= S[j][0] = 1 và S[i][j] = S[i-1][j]+S[i][j-1]
    Tính ma trận S. chọn điểm cuối là điểm cần tìm'''
n  = int(input("nhap size: "))
r = [1]* (n+1)
M=[]
for i in range(n+1):
    M.append(r)
#tinh cac phan tu trong ma tran
for i in range(1,n+1):
    for j in range(1,n+1):
        M[i][j] = M[i-1][j]+M[i][j-1]
# so cac den diem cuoi la phan tu M[n][n]
print(M[n][n])
