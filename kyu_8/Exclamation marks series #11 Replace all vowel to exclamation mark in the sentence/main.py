# Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence

# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/python

def replace_exclamation(st):
    return ''.join(s if s.lower() not in 'aeiou' else '!' for s in st)
