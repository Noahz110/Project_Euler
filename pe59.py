'''common characters in english is 32-93 ,97-122
key is 3 digits from 97-122
a XOR b = a ^ b'''
import time
start = time.time()
test_case = list(range(32,94)) + list(range(97,123))
#code here
with open('p059_cipher.txt', 'rt') as f:
    contents = f.read()
encrypted_text = [int(i) for i in contents.strip().split(',')]
keys = []
for key1 in range(97,123):
    for ascii_num in encrypted_text[::3]:
        if key1 ^ ascii_num not in test_case:
            break
    else:
        keys.append((key1,1))
    for ascii_num in encrypted_text[1::3]:
        if key1 ^ ascii_num not in test_case:
            break
    else:
        keys.append((key1,2))
    for ascii_num in encrypted_text[2::3]:
        if key1 ^ ascii_num not in test_case:
            break
    else:
        keys.append((key1,3))
keys.sort(key=lambda x:x[1])
print(keys)
result = ''
for i in range(len(encrypted_text)):
    if i % 3 == 0:
        result += chr(encrypted_text[i] ^ keys[0][0])
    elif i %3 == 1:
        result += chr(encrypted_text[i] ^ keys[1][0])
    else:
        result += chr(encrypted_text[i] ^ keys[2][0])
print(result)
print(sum([ord(i) for i in result]))
end = time.time()
print('times = {} s'.format(end - start))