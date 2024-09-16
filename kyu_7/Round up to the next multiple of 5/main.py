# Round up to the next multiple of 5

# https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/python

def round_to_next5(n):
    return n // 5 * 5 + (5 if n % 5 else 0)
