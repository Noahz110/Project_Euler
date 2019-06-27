'''{a,b,c} gs a<b a+b+c =p suy ra a<p/3<c'''
import time
start = time.time()

#code here
count_max , p_max = 0, 0 
for p in range(12,1001):
    li = []
    for c in range(int(p/3)+1, p):
        for a in range(1,int(p/3)+1):
            if a ** 2 +(p-a-c) ** 2 == c ** 2:
                li.append((a, p-a-c, c))
    if len(li) > count_max:
        count_max, p_max = len(li) , p

print(count_max,p_max)

end = time.time()
print('times = {} s'.format(end - start))