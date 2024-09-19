# Vowel remover

# https://www.codewars.com/kata/5547929140907378f9000039/train/python

def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')
