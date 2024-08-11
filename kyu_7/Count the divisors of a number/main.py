# Count the divisors of a number

# https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python

def divisors(n):
    return len([x for x in range(1, n + 1) if n % x == 0])

