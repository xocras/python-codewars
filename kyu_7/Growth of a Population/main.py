# Growth of a Population

# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python

def nb_year(p0, percent, aug, p):
    n = 0
    while p0 < p:
        n += 1
        p0 += int(p0 * percent/100 + aug)
    return n

