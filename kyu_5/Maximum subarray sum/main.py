# Maximum subarray sum

# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

def max_sequence(arr):
    maximum_sum = current_sum = 0
    
    for n in arr:
        current_sum = max(n, current_sum + n)
        maximum_sum = max(current_sum, maximum_sum)
        
    return maximum_sum


