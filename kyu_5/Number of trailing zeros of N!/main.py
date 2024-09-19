# Number of trailing zeros of N!

# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

def zeros(n):
    
    count, pow_5 = 0, 5
    
    while pow_5 <= n:
        count += n // pow_5
        pow_5 *= 5
    
    return count
