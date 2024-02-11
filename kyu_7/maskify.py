# Credit Card Mask

# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(cc):
    return cc if len(cc) < 4 else cc[-4:].rjust(len(cc),'#')
