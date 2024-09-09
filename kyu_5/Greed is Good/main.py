# Greed is Good

# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):
    
    points = 0
    
    for n in set(dice):
        
        points += (n if n > 1 else 10) * 100 if dice.count(n) >= 3 else 0
        
    points += dice.count(1) % 3 * 100
    points += dice.count(5) % 3 * 50
    
    return points

