# Find the odd int

# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    for n in seq:
        if seq.count(n) % 2:
            return n
