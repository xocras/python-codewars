# Descending Order

# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def descending_order(num):
    num = [n for n in str(num)]
    num.sort(reverse=True)
    return int(''.join(num))
