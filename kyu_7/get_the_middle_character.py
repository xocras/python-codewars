# Get the Middle Character

# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

def get_middle(s):
    start = (len(s) - 1) / 2 if len(s) % 2 else len(s) / 2 - 1

    end = start + (1 if len(s) % 2 else 2)

    return s[int(start):int(end)]
