# What's the real floor?

# https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python

def get_real_floor(n):
    return len([floor for floor in range(n) if floor not in [0, 13]]) if n >= 0 else n
