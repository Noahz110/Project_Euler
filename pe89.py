'''basiclly we just need to find VIIII,IIII,LXXXX,XXXX,DCCCC,CCCC and replace by
IX,IV,XC,XL,CM,CD then number of characters saved are 3,2,3,2,3,2 respectively
find total all the number of char saved'''
import time
start = time.time()

#code here
with open('p089_roman.txt', 'rt') as f:
    data = f.readlines()
li = [d.strip() for d in data]
d = {
'I' : 1,
'V' : 5,
'X' : 10,
'L' : 50,
'C' : 100,
'D' : 500,
'M' : 1000,
}
count = 0
for number in li:
    if 'VIIII' in number:
        count += 3
    elif 'IIII' in number:
        count += 2
    if 'LXXXX' in number:
        count += 3
    elif 'XXXX' in number:
        count += 2
    if 'DCCCC' in number:
        count += 3
    elif 'CCCC' in number:
        count += 2
print(count)

end = time.time()
print('times = {} s'.format(end - start))