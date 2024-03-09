# Is a number prime?

# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python

def is_prime(num):
    if num < 2 or (num % 2 == 0 and num != 2):
        return False

    for divisor in range(3, int(num ** 0.5) + 1, 2):
        if num % divisor == 0:
            return False

    return True