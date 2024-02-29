# Categorize New Member

# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

def open_or_senior(data):
    return ['Senior' if age > 54 and hc > 7 else 'Open' for age, hc in data]
