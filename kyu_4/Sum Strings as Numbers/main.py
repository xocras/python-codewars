# Sum Strings as Numbers

# https://www.codewars.com/kata/5324945e2ece5e1f32000370/train/python

def sum_strings(x, y):
    
    max_length = max(len(x), len(y))
    
    x = x.zfill(max_length)
    y = y.zfill(max_length)
    
    carry = 0
    
    result = ''
    
    for i in range(max_length - 1, -1, -1):
        
        added_digits = int(x[i]) + int(y[i]) + carry
        
        carry = added_digits // 10
        
        result += str(added_digits % 10)
        
    result += str(carry) if carry else ''
    
    result = result[::-1].lstrip('0')
        
    return result if result else '0'
