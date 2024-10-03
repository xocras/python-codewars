# Give me a Diamond

# https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python

def diamonds(n):
    if n < 1 or not n % 2:
        return None
    
    diamond = [x for x in range(1, n + 1, 2)] + [x for x in range(n - 2, 0, -2)]
    
    diamond = [("*" * x).center(n).rstrip() + '\n' for x in diamond]

    return ''.join(diamond)
