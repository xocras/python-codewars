# Roman Numerals Encoder

# https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

def solution(n):
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    
    roman_representation  = ''
    for amount in roman_numerals:
        while n >= amount:
            roman_representation += roman_numerals[amount]
            n -= amount
    
    return roman_representation

