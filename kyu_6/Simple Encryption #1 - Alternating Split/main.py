# Simple Encryption #1 - Alternating Split

# https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python

def decrypt(text, n):
    for _ in range(n):
        
        left = text[:len(text) // 2]
        right = text[len(text) // 2:]
        
        text = ''.join(r_c + l_c for l_c, r_c in zip(left, right))
        
        text += right[-1] if len(right) - len(left) else ''
        
    return text


def encrypt(text, n):
    
    for _ in range(n):
        
        text = text[1::2] + text[::2]
    
    return text
