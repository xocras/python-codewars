# Which are in?

# https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

def in_array(array1, array2):
    return sorted(set([x for x in array1 if x in ' '.join(array2)]))

