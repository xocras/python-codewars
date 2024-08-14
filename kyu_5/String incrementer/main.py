# String incrementer

# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

import re

def increment_string(strng):
    
    match = re.search(r'(.*?)(\d+)$', strng)
    
    if match:
        s = match.group(1)
        n = f"{int(match.group(2) or 0) + 1}".zfill(len(match.group(2))) 
    else:
        s = strng
        n = "1"
    
    return s + n

