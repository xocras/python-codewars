# Directions Reduction

# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

def dir_reduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []

    for direction in arr:
        stack.pop() if stack and stack[-1] == opposites.get(direction) else stack.append(direction)

    return stack
            
        

