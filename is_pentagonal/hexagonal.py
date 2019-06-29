import math
def is_pentagonal(n):
    s = (1+math.sqrt(24*n+1))/6
    return int(s)== s

def is_hexagonal(n):
    s = (1+math.sqrt(8*n+1))/4
    return int(s) == s
