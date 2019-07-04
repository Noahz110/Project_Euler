'''9**2 *7 = 567
xet cac so <568 chia ra 2 list
runtime 42s not bad xD'''
import time
start = time.time()

#code here
count = 0
li_1 =[]
li_89 = []
for numb in range(1,568):
    new_numb = numb
    while True:
        new_numb = sum([int(i)**2 for i in str(new_numb)])
        if new_numb == 1:
            li_1.append(numb)
            break
        elif new_numb == 89:
            li_89.append(numb)
            break
count1 = 0
for i in range(1,10000000):
    if sum(int(j)**2 for j in str(i)) in li_1:
        count1 +=1

print(10**7-1 - count1)
end = time.time()
print('times = {} s'.format(end - start))