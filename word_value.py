import string
def word_value(word):
    return sum([string.ascii_lowercase.index(i) + 1 for i in word.lower()])
