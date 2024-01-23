# Multiples of 3 or 5
from functools import reduce


# v1.0
def solution(number):
    if number < 0:
        return 0
    total = 0
    for n in range(number):
        if not n % 3 or not n % 5:
            total += n
    return total


# v2.0
def solution_v2(number):
    return 0 if number < 0 else reduce(lambda a, b: a + (b if not b % 3 or not b % 5 else 0), range(number), 0)
