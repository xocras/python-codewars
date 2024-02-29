# Your order, please

# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

import re


def order(sentence):
    return ' '.join(sorted([word for word in sentence.split()], key=lambda x: re.findall(r'\d', x)[0]))
