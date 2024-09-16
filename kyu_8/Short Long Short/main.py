# Short Long Short

# https://www.codewars.com/kata/50654ddff44f800200000007/train/python

def solution(a, b):
    return b + a + b if len(a) > len(b) else a + b + a
