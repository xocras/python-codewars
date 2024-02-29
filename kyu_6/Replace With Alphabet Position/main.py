# Replace With Alphabet Position

# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def alphabet_position(text):
    alphabet = [*'abcdefghijklmnopqrstuvwxyz']

    return ' '.join([str(alphabet.index(x) + 1) for x in text.lower() if x in alphabet])
