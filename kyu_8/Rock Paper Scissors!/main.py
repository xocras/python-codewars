# Rock Paper Scissors!

# https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python

def rps(p1, p2):
    x = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if x[p1] == p2:
        return "Player 1 won!"
    if x[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

