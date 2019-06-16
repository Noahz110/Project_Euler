pali = 0
for i in range(100,1000):
    for x in range(100,1000):
        tem = x * i
        s = str(tem)
        if s == s[::-1] and tem > pali:
            pali = tem
print(pali)

