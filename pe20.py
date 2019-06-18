t = int(input("nhap vao t: "))
prod = 1
total= 0
for i in range(1,t+1):
    prod *= i
prod = str(prod)
for i in prod:
    total += int(i)
print(total)