import time
start = time.time()

#code here
coins = [1, 2, 5, 10, 20, 50, 100, 200]
t= 200
cnt = 2
h=0
for g in range(2):
    pg = t - 100 * g
    for f in range(pg//50 +1):
        pf = pg - 50* f
        for e in range(pf//20+1):
            pe = pf - 20* e
            for d in range(pe//10+1):
                pd = pe -10* d 
                for c in range(pd//5 +1):
                    pc = pd -5* c
                    for b in range(pc//2+1):
                        cnt += 1
                                    
print(cnt)
end = time.time()
print('times = {} s'.format(end - start))