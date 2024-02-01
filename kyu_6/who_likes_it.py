# Who likes it?

# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

def likes(names):
    length = len(names)
    if not length:
        return "no one likes this"
    elif length == 1:
        return f"{names[0]} likes this"
    elif length == 2:
        return f"{names[0]} and {names[1]} like this"
    elif length == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {length - 2} others like this"
