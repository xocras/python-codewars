# Detect Pangram

# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

def is_pangram(s):
    return len(set(c.lower() for c in s if c.isalpha())) == 26
