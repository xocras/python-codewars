# Calculate average

# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python

import statistics


def find_average(numbers):
    return statistics.mean(numbers) if numbers else 0

