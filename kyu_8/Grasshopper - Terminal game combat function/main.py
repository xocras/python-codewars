# Grasshopper - Terminal game combat function

# https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/python

def combat(health, damage):
    return health - damage if health > damage else 0
