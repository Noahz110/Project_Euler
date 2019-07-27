'''fucking brutal code. nothing but brute force code'''
import time
start = time.time()

#code here

with open('p054_poker.txt','rt') as f:
    content = f.readlines()
data = [i.strip() for i in content]

# spliting to a list of tuple(player1,player2)
players = [(i.split()[:5], i.split()[5:]) for i in data]

# Sorting cards follow the given order
sort_order2 = '23456789TJQKA'
for player1, player2 in players:
    player1.sort(key=lambda i: sort_order2.index(i[0]))
    player2.sort(key=lambda i: sort_order2.index(i[0]))
# take feature of player: 1 to 10 as ranked.and the highest card to compare if equal
def feature(player):
    f1 = ''
    f2 = ''
    for card in player:
        f1 += card[0]
        f2 += card[1]
    # Royal Flush
    if f1 == 'TJQKA' and len(set(f2)) == 1:
        return [10]
    # Straight Flush
    elif f1 in sort_order2 and len(set(f2)) == 1:
        return [9]
    elif len(set(f1)) == 2:
        # Four of a kind
        if f1.count(list(set(f1))[0]) == 1:
            return [8,list(set(f1))[1],list(set(f1))[0]]
        elif f1.count(list(set(f1))[0]) == 4:
            return [8, list(set(f1))[0], list(set(f1))[1]]
        # Full house
        elif f1.count(list(set(f1))[0]) == 3:
            return [7,list(set(f1))[0],list(set(f1))[1]]
        elif f1.count(list(set(f1))[0]) == 2:
            return [7, list(set(f1))[1], list(set(f1))[0]]
    # Flush
    elif len(set(f2)) == 1:
        return [6]
    # Straight
    elif f1 in sort_order2:
        return [5]
    elif len(set(f1)) == 3:
        # Three of a kind
        li_f1 = sorted(list(set(f1)),key=lambda i: sort_order2.index(i[0]))
        if f1.count(li_f1[0]) == 3:
            return [4, li_f1[0], li_f1[2], li_f1[1]]
        elif f1.count(li_f1[1]) == 3:
            return [4, li_f1[1], li_f1[2], li_f1[0]]
        elif f1.count(li_f1[2]) == 3:
            return [4, li_f1[2], li_f1[1], li_f1[0]]
        # two pairs
        elif f1.count(li_f1[0]) == 1:
            return [3, li_f1[2], li_f1[1], li_f1[0]]
        elif f1.count(li_f1[1]) == 1:
            return [3, li_f1[2], li_f1[0], li_f1[1]]
        elif f1.count(li_f1[2]) == 1:
            return [3, li_f1[1], li_f1[0], li_f1[2]]
    # A pair
    elif len(set(f1)) == 4:
        li_f1 = sorted(list(set(f1)),key=lambda i: sort_order2.index(i))
        for i in li_f1:
            if f1.count(i) == 2: 
                result = [2,i]
                li_f1.remove(i)
                result.extend(li_f1[::-1])
                return result
    # High card
    else:
        return [1]

def index(a):
    return sort_order2.index(a)


cnt = 0
for player1, player2 in players:
    if feature(player1)[0] > feature(player2)[0]:
        cnt += 1
    elif feature(player1)[0] == feature(player2)[0]:
        if feature(player1)[0] == 9:
            if index(player1[-1][0]) > index(player2[-1][0]):
                cnt += 1
        elif feature(player1)[0] == 8:
            if index(feature(player1)[1]) > index(feature(player2)[1]):
                cnt+=1
            elif index(feature(player1)[1]) == index(feature(player2)[1]):
                if index(feature(player1)[2]) > index(feature(player2)[2]):
                    cnt+=1
        elif feature(player1)[0] == 7:
            if index(feature(player1)[1]) > index(feature(player2)[1]):
                cnt+=1
            elif index(feature(player1)[1]) == index(feature(player2)[1]):
                if index(feature(player1)[2]) > index(feature(player2)[2]):
                    cnt+=1
        elif feature(player1)[0] == 6:
            if index(player1[-1][0]) > index(player2[-1][0]):
                cnt+=1
        elif feature(player1)[0] == 5:
            if index(player1[-1][0]) > index(player2[-1][0]):
                cnt+=1
        elif feature(player1)[0] == 4:
            if feature(player1)[1] > feature(player2)[1]:
                cnt +=1
            elif feature(player1)[1] == feature(player2)[1]:
                if feature(player1)[2] > feature(player2)[2]:
                    cnt +=1
                elif feature(player1)[2] == feature(player2)[2]:
                    if feature(player1)[3] > feature(player2)[3]:
                        cnt +=1
        elif feature(player1)[0] == 3:
            if feature(player1)[1] > feature(player2)[1]:
                cnt +=1
            elif feature(player1)[1] == feature(player2)[1]:
                if feature(player1)[2] > feature(player2)[2]:
                    cnt +=1
                elif feature(player1)[2] == feature(player2)[2]:
                    if feature(player1)[3] > feature(player2)[3]:
                        cnt +=1
        elif feature(player1)[0] == 2:
            for i in range(1,5):
                if index(feature(player1)[i]) > index(feature(player2)[i]):
                    cnt+=1
                    break
                elif index(feature(player1)[i]) < index(feature(player2)[i]):
                    break
        elif feature(player1)[0] == 1:
            if index(player1[-1][0]) > index(player2[-1][0]):
                cnt +=1

print(cnt)

end = time.time()
print('times = {} s'.format(end - start))


