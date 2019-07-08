import time
start = time.time()
from is_polygonal import is_heptagonal, is_hexagonal, is_octagonal, is_pentagonal, is_square, is_triangle

list_hep = [i for i in range(1000,10000) if is_heptagonal(i)]
list_hex = [i for i in range(1000,10000) if is_hexagonal(i)]
list_oct = [i for i in range(1000,10000) if is_octagonal(i)]
list_pen = [i for i in range(1000,10000) if is_pentagonal(i)]
list_sqrt = [i for i in range(1000,10000) if is_square(i)]
list_tri = [i for i in range(1000,10000) if is_triangle(i)]

def find_set():
    for hep in list_hep:
        for hex in list_hex:
            for oct in list_oct:
                for pen in list_pen:
                    for sqr in list_sqrt:
                        for tri in list_tri:
                            front = sorted([hep//100,hex//100,oct//100,pen//100,sqr//100,tri//100])
                            back = sorted([hep%100,hex%100,oct%100,pen%100,sqr%100,tri%100])
                            if front == back:
                                return hep,hex,oct,pen,sqr,tri

print(find_set())

end = time.time()
print('times = {} s'.format(end - start))