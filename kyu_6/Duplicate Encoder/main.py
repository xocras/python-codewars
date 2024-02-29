# Duplicate Encoder

# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    return ''.join([")" if word.lower().count(x) > 1 else "(" for x in word.lower()])
