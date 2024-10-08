# Build a pile of Cubes

# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

def find_nb(m):
    # Sum of Cubes
    n = int((2 * m ** 0.5) ** 0.5)
    # Check Volume
    return n if n * (n + 1) // 2 * n * (n + 1) // 2 == m else -1

