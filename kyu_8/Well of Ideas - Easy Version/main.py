# Well of Ideas - Easy Version

# https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python

def well(x):
    return 'Fail!' if 'good' not in x else 'Publish!' if x.count('good') <= 2 else 'I smell a series!'
