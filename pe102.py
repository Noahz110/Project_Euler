'''if O inside ABC so SABC = SOAB + SOCA + SOBC
Sabc = AB.AC.sinA. can google that'''
import time
start = time.time()

#code here
with open('p102_triangles.txt','r') as f:
    cnt = 0
    for line in f:
        coor_str = line.strip().split(',')
        coor_int = [int(i) for i in coor_str]
        xa, ya, xb, yb, xc, yc = tuple(coor_int)
        Sabc = abs((xb-xa)*(yc-ya)-(xc-xa)*(yb-ya))/2
        Soab = abs((xb-0)*(ya-0)-(xa-0)*(yb-0))/2
        Socb = abs((xb-0)*(yc-0)-(xc-0)*(yb-0))/2
        Soac = abs((xc-0)*(ya-0)-(xa-0)*(yc-0))/2
        if Sabc == Soab + Soac + Socb:
            cnt += 1

print(cnt)

end = time.time()
print('times = {} s'.format(end - start))