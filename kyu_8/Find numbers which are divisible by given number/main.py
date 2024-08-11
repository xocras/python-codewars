# Find numbers which are divisible by given number

# https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python

def divisible_by(numbers, divisor):
    return [n for n in numbers if not n % divisor]

