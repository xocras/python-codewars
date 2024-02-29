# Range Extraction

# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

def solution(args):

    ranges, group = [], []

    for i, n in enumerate(args):

        if not i or n - 1 == args[i - 1]:
            group.append(n)
            continue

        ranges.append(group)
        group = [n]

    ranges.append(group)

    return ','.join(
        f'{x[0]}-{x[-1]}' if len(x) > 2 else
        f'{x[0]},{x[-1]}' if len(x) > 1 else
        f'{x[0]}'
        for x in ranges
    )
