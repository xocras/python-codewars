# Count the Digit

# https://www.codewars.com/kata/566fc12495810954b1000030/train/python

def nb_dig(n, d):
    return ''.join(str(k ** 2) for k in range(n + 1)).count(str(d))

