# WeIrD StRiNg CaSe

# https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python

def to_weird_case(words):
    return ' '.join(''.join(c.lower() if i % 2 else c.upper() for i, c in enumerate(word)) for word in words.split())
