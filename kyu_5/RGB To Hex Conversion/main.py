# RGB To Hex Conversion

# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

def rgb(r, g, b):
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    
    return f"{r:02X}{g:02X}{b:02X}"

