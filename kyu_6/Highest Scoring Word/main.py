# Highest Scoring Word

# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def high(x):
    scores = [sum(ord(c) - 96 for c in w) for w in x.split()]
    
    return x.split()[scores.index(max(scores))]

