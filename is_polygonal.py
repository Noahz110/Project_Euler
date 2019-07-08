import math
def is_triangle(n):
    s = (math.sqrt(8*n+1)-1)/2
    return int(s) == s

def is_square(n):
    s = math.sqrt(n)
    return int(s) == s

def is_pentagonal(n):
    s = (1+math.sqrt(24*n+1))/6
    return int(s)== s

def is_hexagonal(n):
    s = (1+math.sqrt(8*n+1))/4
    return int(s) == s

def is_heptagonal(n):
    s = (math.sqrt(9+40*n)+3)/10
    return int(s) == s

def is_octagonal(n):
    s = (math.sqrt(1+3*n)+1)/3
    return int(s) == s