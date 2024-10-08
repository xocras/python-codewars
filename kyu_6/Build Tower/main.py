# Build Tower

# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(n_floors):
    tower = ['*' + '*' * n * 2 for n in range(n_floors)]
    
    return [floor.center(len(tower[-1])) for floor in tower]

