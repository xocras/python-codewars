# Consecutive strings

# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
    return max([''.join(strarr[i : k + i]) if k + i <= len(strarr) else x for i, x in enumerate(strarr)],key=len) if strarr and 0 < k <= len(strarr) else ''

