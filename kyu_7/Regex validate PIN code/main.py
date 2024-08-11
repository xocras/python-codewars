# Regex validate PIN code

# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python

def validate_pin(pin):
    return pin.isnumeric() and len(pin) in [4, 6]

