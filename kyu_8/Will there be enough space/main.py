# Will there be enough space?

# https://www.codewars.com/kata/5875b200d520904a04000003/train/python

def enough(cap, on, wait):
    return max(0, wait - (cap - on))

