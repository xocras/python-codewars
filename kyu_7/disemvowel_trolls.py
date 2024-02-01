# Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string_):
    return "".join(c for c in string_ if c.lower() not in "aeiou")
