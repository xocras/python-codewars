# Opposites Attract

# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

def lovefunc( flower1, flower2 ):
    return (flower1 % 2 == 1 and not flower2 % 2) or (flower2 % 2 == 1 and not flower1 % 2)

