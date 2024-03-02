# Delete occurrences of an element if it occurs more than n times

# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

def delete_nth(order,max_e):
    arr = []
    
    for x in order:
        if arr.count(x) < max_e:
            arr.append(x)
            
    return arr

