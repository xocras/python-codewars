# Valid Braces

# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

def valid_braces(string):
    stack, braces = [], {")": "(", "]": "[", "}": "{"}

    for x in string:
        if x in braces.values():
            stack.append(x)
        elif x in braces.keys():
            if not stack or stack[-1] != braces[x]:
                return False
            stack.pop()
        else:
            return False

    return not stack
