# Shortest Word

# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

def find_short(s):
    return len(sorted(s.split(), key=len)[0])
