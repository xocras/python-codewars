# Expressions Matter

# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python

def expression_matter(a, b, c):
    return max(a * (b + c), (a + b) * c, a * b * c, a + b + c)


