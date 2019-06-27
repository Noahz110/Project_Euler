def is_pandigital(n):
    if len(n) != 9:
        return False
    else:
        li = [i for i in n]
        li.sort()
        if li == ['1','2','3','4','5','6','7','8','9']:
            return True
        else:
            return False
