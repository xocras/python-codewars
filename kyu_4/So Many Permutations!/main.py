# So Many Permutations!

# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python

from itertools import permutations as pm


def permutations(s):
    return list(set(map("".join, pm(s))))
