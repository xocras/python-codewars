# Find the missing letter

# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

def find_missing_letter(chars):
    alphabet = [*'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    
    start = alphabet.index(chars[0].upper())
    
    for i, j in zip(range(start, start + len(chars)), range(0, len(chars))):
        if alphabet[i].upper() != chars[j].upper():
            return alphabet[i] if chars[0].isupper() else alphabet[i].lower()
    



