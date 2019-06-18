zero = ['one','two','three','four','five','six','seven','eight','nine']
ten = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
hundred = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
string = ''
tem = ''
def mot_tram(i):
    if i < 10:
        return zero[(i%10)-1]
    elif i % 10 == 0:
        return hundred[int(i/10) -1]
    elif i < 20:
        return ten[(i%10)-1]
    else:
        tem = hundred[int(i/10)-1] + zero[(i%10)-1]
        return tem

for i in range(1,1001):
    if i == 1000:
        tem = 'onethousand'
        string = string + tem
    elif i % 100 == 0:
        tem = zero[int(i/100) - 1] + 'hundred'
        string += tem
    elif i < 100:
        string += mot_tram(i)
    else:
        tem = zero[int(i/100) - 1] + 'hundred'+ 'and' + mot_tram(i%100)
        string += tem
print(len(string))