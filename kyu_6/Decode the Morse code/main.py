# Decode the Morse code

# https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python

# from preloaded import MORSE_CODE

MORSE_CODE = {}


def decode_morse(morse_code):
    return ' '.join([''.join([MORSE_CODE.get(c) for c in word.split()]) for word in morse_code.split('   ')]).strip()
