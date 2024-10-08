# Human Readable Time

# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f'{h:02d}:{m:02d}:{s:02d}'

