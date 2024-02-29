# Playing with digits

# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
    r = sum(int(n) ** (p + i) for i, n in enumerate(str(n))) / n
    return r if r == int(r) else -1
