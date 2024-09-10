# Make a function that does arithmetic!

# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python

def arithmetic(a, b, operator):
    return {"add": a + b, "subtract": a - b, "multiply": a * b, "divide": a / b}[operator]
