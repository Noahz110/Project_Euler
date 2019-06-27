import time
start = time.time()

import string
def word_value(word):
    return sum([string.ascii_lowercase.index(i) + 1 for i in word.lower()])

import math
def is_triangle_number(n):
    for i in range(1,int(math.sqrt(2*n)) + 1):
        if 2 * n == i* (i + 1):
            return True
    return False
#code here
file = open("p042_words.txt",'rt')
contents = file.read()
words = [i.strip('"') for i in contents.split(',')]
count = 0
for word in words:
    if is_triangle_number(word_value(word)):
        count += 1

print(count)
end = time.time()
print('times = {} s'.format(end - start))