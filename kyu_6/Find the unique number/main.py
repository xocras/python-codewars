# Find the unique number

# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
    unique = set(arr)
    for x in unique:
        if arr.count(x) == 1:
            return x

