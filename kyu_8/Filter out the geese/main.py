# Filter out the geese

# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return [x for x in birds if x not in geese]
