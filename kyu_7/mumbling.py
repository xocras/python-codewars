# Mumbling

# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accum(st):
    return '-'.join([(c * (i + 1)).title() for i, c in enumerate(st)])

