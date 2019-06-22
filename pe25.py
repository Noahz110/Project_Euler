import time
start = time. time()

cnt = 2
a1 = 1
a2 = 1
while True:
    cnt += 1
    F = a1 + a2
    if len(str(F)) > 999:
        break
    a1 = a2
    a2 = F 
print(cnt)

end = time. time()
print('times = {} s'.format(end - start))