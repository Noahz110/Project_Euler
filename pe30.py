'''giả sử a có n chữ số: 9^5 * n > a
suy ra 9^5 * 6 = 354294 < 999999 
như vậy a sữ có nhiều nhất 6 chữ số'''
li=[]
total = 0
for a in range(2,1000000):
    if a ==  sum([int(i)**5 for i in str(a)]):
        li.append(a)
        total += a
print(total)
print(li)