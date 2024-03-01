# Printer Errors

# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    colors = [chr(i) for i in range(ord('a'), ord('n'))]
    return f'{len([e for e in s if e not in colors])}/{len(s)}'

