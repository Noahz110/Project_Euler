def is_reversible(number):
    reversed_number = str(number)[::-1]
    if reversed_number[0] == '0':
        return False
    reversed_sum = number + int(reversed_number)
    reversible = [int(x) for x in str(reversed_sum)]
    return all(x % 2 != 0 for x in reversible)

print(len([i for i in range(1, 10**7) if is_reversible(i)]))