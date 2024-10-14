# Two fighters, one winner.

# https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/train/python

def declare_winner(fighter1, fighter2, attacker):
    
    while fighter1.health > 0 and fighter2.health > 0:
        
        if attacker == fighter1.name:
            fighter2.health -= fighter1.damage_per_attack 
            if fighter2.health > 0:
                attacker = fighter2.name 
        else:
            fighter1.health -= fighter2.damage_per_attack 
            if fighter1.health > 0:
                attacker = fighter1.name 

    return attacker
