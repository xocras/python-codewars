# Convert number to reversed array of digits

# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

def digitize(n):
    return [int(n) for n in str(n)[::-1]]

