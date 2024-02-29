# Tribonacci Sequence

# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

def tribonacci(signature, n):
    for _ in range(n - 3):
        signature.append(sum(signature[-3:]))
    return signature[:n]
