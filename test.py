from fractions import Fraction as F
fracs = []
for d in range(2,80):
    for n in range(1,d):
        a = F(n,d)
        if a not in fracs:
            fracs.append(a)
fracs.sort()
print(fracs.index(F(1,3)), len(fracs))