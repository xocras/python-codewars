# Weight for weight

# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def order_weight(strng): 
    
    return ' '.join(sorted(sorted(strng.split()), key=lambda x : sum(int(c) for c in x)))

