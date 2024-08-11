# Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!

# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python

def sum_dig_pow(a, b): 
    return [x for x in range(a, b + 1) if sum(int(digit) ** i for i, digit in enumerate(str(x), 1)) == x]

