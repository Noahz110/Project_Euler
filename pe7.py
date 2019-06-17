t = int(input("Nhap so thu tu :"))
li = [2]
for i in range(2,t+1):
    li.append(li[-1])
    while True:
        li[-1] = li[-1] + 1
        for x in li[:-2]:
            if li[-1] % x == 0:
                break
        else:
            break
print(li[-1])
