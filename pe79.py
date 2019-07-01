import time
start = time.time()

#code here
with open('p079_keylog.txt','rt') as f:
    contents = f.read()

numbers = contents.splitlines()
print(numbers)

end = time.time()
print('times = {} s'.format(end - start))