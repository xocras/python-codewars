# Convert string to camel case

# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

import re


def to_camel_case(text):
    return re.sub(r'[-_](\w)', lambda x: x.group(1).upper(), text)
