# How good are you really?

# https://www.codewars.com/kata/5601409514fc93442500010b/train/python

import statistics


def better_than_average(class_points, your_points):
    return statistics.mean(class_points) < your_points

