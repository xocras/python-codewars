# Simple Fun #176: Reverse Letter

# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/python

def reverse_letter(st):
    return ''.join(s for s in st if s.isalpha())[::-1]
