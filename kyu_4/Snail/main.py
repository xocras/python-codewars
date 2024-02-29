# Snail

# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

def snail(snail_map):
    result = []

    while snail_map:
        # Take the first row
        result += snail_map.pop(0)

        # Take the last element of each remaining row
        if snail_map and snail_map[0]:
            for row in snail_map:
                result.append(row.pop())

        # Take the last row in reverse order
        if snail_map:
            result += snail_map.pop()[::-1]

        # Take the first element of each remaining row in reverse order
        if snail_map and snail_map[0]:
            for row in reversed(snail_map):
                result.append(row.pop(0))

    return result