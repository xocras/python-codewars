# Remove the minimum

# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python

def remove_smallest(numbers):
    return [n for i, n in enumerate(numbers) if not numbers.index(min(numbers)) == i]

