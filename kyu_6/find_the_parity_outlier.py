# Find The Parity Outlier

# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    odd = (integers[0] % 2 and integers[1] % 2) or (integers[1] % 2 and integers[2] % 2) or (integers[0] % 2 and integers[2] % 2)
    return list(filter(lambda n: not n % 2 if odd else n % 2, integers))[0]