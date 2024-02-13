# Beginner Series #3 Sum of Numbers

# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a,b):
    return sum(range(b, a - 1, -1) if a < b else range(a, b - 1, -1))

# def get_sum(a,b):
#     return sum(range(min(a, b), max(a, b) + 1))
