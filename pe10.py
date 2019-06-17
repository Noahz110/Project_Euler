import math
li = [2]
t = int(input("Nhap max :"))
def isprime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n % i == 0:
            return False    
    return True  
for y in range(3, t):
    if isprime(y) == True:
        li.append(y)
print(sum(li))
# 5s