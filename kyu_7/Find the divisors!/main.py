# Find the divisors!

# https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python

def divisors(integer):
    return [n for n in range(2, integer) if not integer % n] or f'{integer} is prime'
    

