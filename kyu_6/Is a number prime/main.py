# Is a number prime?

# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python

def is_prime(num):
    if num < 2 or (not num % 2 and num != 2):
        return False

    for n in range(3, int(num ** 0.5) + 1, 2):
        if not num % n:
            return False

    return True
