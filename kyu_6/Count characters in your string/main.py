# Count characters in your string

# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

def count(s):
    return {x: s.count(x) for x in set(s)}

