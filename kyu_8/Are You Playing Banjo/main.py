# Are You Playing Banjo?

# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

def are_you_playing_banjo(name):
    return name + (' plays' if name.upper()[0] == "R" else ' does not play') + ' banjo'

