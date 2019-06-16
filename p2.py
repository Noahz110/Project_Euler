li= [1,2]
sum = 0
while li[-1] <= 4000000:
    li.append(li[-2]+li[-1])
for i in li:
    if i % 2 == 0:
        sum = sum + i
print(sum)