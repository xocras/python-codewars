# Money, Money, Money

# https://www.codewars.com/kata/563f037412e5ada593000114/train/python

def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal *= (1 + interest * (1 - tax))
        years += 1 
    return years
