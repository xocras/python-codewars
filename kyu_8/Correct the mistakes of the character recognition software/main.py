# Correct the mistakes of the character recognition software

# https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python

def correct(s):
    return ''.join({'5':'S','0':'O','1':'I'}.get(x, x) for x in s)

