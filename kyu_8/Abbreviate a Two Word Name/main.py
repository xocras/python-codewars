# Abbreviate a Two Word Name

# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

def abbrev_name(name):
    return '.'.join(x[0].upper() for x in name.split())

