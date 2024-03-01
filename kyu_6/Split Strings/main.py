# Split Strings

# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

def solution(s):
    result = [s[i:i+2] for i in range(0, len(s)-1, 2)]
    if len(s) % 2 != 0:
        result.append(s[-1] + '_')
    return result
        

