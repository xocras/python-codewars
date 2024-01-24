# Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

from functools import reduce


def get_count(sentence):
    return reduce(lambda a, b: a + sentence.count(b), [*"aeiou"], 0)
