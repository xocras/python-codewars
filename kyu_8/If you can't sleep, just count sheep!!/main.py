# If you can't sleep, just count sheep!!

# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python

def count_sheep(n):
    return ''.join(f'{i + 1} sheep...' for i in range(n))

