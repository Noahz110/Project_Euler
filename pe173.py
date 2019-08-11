'''m,n is width out and in of a square lamina => tiles = m*m - n*n
m-n always divided by 2
m_max**2 = k_max * (m_max-2)**2 '''
import time
start = time.time()

#code here
k_max = 1000000
m_max = k_max//4 + 1
cnt = 0
for m in range(3,m_max+1):
    for n in range(m - 2, 0 , -2):
        if (m**2 - n**2) > k_max:
            break
        cnt += 1

print(cnt)

end = time.time()
print('times = {} s'.format(end - start))