# Moving Zeros To The End

# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):
    return sorted(lst, key=lambda n: n > 0, reverse=True)
