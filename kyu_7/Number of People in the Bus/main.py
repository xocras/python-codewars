# Number of People in the Bus

# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

def number(bus_stops):
    return sum(x - y for x, y in bus_stops)

