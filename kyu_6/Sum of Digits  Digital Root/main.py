# Sum of Digits / Digital Root

# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    if len(str(n)) > 1:
        return digital_root(sum([int(digit) for digit in str(n)]))
    return n
