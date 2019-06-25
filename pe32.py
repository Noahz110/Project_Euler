''' a= b*c (gia su b<c)
a chỉ có thể có 4 chữ số.
vì nếu a có 3 chữ số thì b,c 3 chữ số => b*c >a
nếu a có 5 chữ số thì b,c chia ra có 4 chữ số => max(b*c) = 98 * 76 =7448 < a
=> a có 4 => b,c có 5 = 1+4=2+3'''

import time
start = time.time()

#code here
products = []
lia =[]
nums = ['1','2','3','4','5','6','7','8','9']
for b in range(1,99):
    lib =[i for i in str(b)]
    for c in range(12,9877):
        lic = lib + [i for i in str(c)]
        a = b * c
        if len(str(a)) == 9 - len(str(b)) - len(str(c)):
            for i in str(a):
                if i not in lic and i != '0':
                    lic.append(i)
            lic.sort()
            if lic == nums and a not in products:
                products.append(a)

print(sum(products))
            


end = time.time()
print('times = {} s'.format(end - start))