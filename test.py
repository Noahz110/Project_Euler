prod =1
for i in range(1,7255):
    if 7254 % i == 0:
        prod *= i
print(prod)