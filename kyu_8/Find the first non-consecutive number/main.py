# Find the first non-consecutive number

# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python

def first_non_consecutive(arr):
    for i, n in enumerate(arr[1:],1):
        if arr[i - 1] + 1 != n:
            return n

