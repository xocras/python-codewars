# Find the unique string

# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3/train/python

def find_uniq(arr):
    
    unique = [''.join(sorted(set(x.lower().strip()))) for x in arr]
    
    a, b = set(unique)
    
    x = a if unique.count(b) > 1 else b
    
    return arr[unique.index(x)]

