# Find the stray number

# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python

def stray(arr):
    for x in set(arr):
        if arr.count(x) == 1:
            return x

