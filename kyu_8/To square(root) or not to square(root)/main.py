# To square(root) or not to square(root)

# https://www.codewars.com/kata/57f6ad55cca6e045d2000627/train/python

def square_or_square_root(arr):
    return [x ** 0.5 if (x ** 0.5).is_integer() else x ** 2 for x in arr]

