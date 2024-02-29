# Square sums (simple)

# https://www.codewars.com/kata/5a6b24d4e626c59d5b000066/train/python

import math


def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n


def square_sums_row(n):
    def backtrack(arr):
        # Completed Sequence
        if len(arr) == n:
            return arr

        for x in range(1, n + 1):
            if x not in arr:
                # If sequence is empty or the sum of the current
                # and previous number are perfect squares...
                if not arr or is_perfect_square(x + arr[-1]):
                    arr.append(x)
                    result = backtrack(arr)
                    if result:
                        return result
                    arr.pop()
        return False

    return backtrack([])
