# Roman Numerals Decoder

# https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

def solution(roman : str) -> int:
    
    roman_numerals = {
        "M": 1000,
        "CM": -200,
        "D": 500,
        "CD": -200,
        "C": 100,
        "XC": -20,
        "L": 50,
        "XL": -20,
        "X": 10,
        "IX": -2,
        "V": 5,
        "IV": -2,
        "I": 1
    }

    return sum(roman.count(numeral) * roman_numerals[numeral]  for numeral in roman_numerals)

