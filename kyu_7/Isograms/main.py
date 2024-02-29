# Isograms

# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    return sum(string.lower().count(x.lower()) for x in string) == len(string)
