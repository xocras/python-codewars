# Unique In Order

# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):
    return [x for i, x in enumerate(sequence) if sequence[i - 1] != x or not i]
