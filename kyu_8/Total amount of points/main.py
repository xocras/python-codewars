# Total amount of points

# https://www.codewars.com/kata/5bb904724c47249b10000131/train/python

def points(games):
    return sum(
        3 if int(x) > int(y) else 1 if x == y else 0 for x, y in (game.split(":") for game in games)
    )


