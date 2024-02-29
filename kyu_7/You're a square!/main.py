# You're a square!

# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

import math

def is_square(n):
    return math.sqrt(n).is_integer() if n >= 0 else False
