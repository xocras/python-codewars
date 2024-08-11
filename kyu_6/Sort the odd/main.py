# Sort the odd

# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(source_array):
    odds = sorted(n for n in source_array if n % 2)
    return [odds.pop(0) if n % 2 else n for n in source_array]

