# Rectangle into Squares

# https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python

def sq_in_rect(l, w):
    
    if l == w:
        return None
    
    squares = []
    
    while l * w > 0:
        
        square = min(l, w)
        
        squares += [square]

        if square == l:
            w -= l
        else:
            l -= w
        
    return squares
