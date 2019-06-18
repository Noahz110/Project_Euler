def d(n):
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    return total
result = 0
for i in range(1,10000):
    if d(d(i)) == i and d(i)!= i:
        result += i
print(result) 