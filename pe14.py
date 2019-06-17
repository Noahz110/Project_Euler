count = 0
max = 1
for i in range(2,1000000):
    li = [i]
    while li[-1] != 1:
        if li[-1] % 2 == 0:
            li.append(int(li[-1]/2))
        else:
            li.append(3 * li[-1] + 1)
    if count < len(li):
        count = len(li)
        max = i
print(max)
