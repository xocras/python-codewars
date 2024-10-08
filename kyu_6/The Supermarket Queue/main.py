# The Supermarket Queue

# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

def queue_time(customers, n):
    
    queue = [0] * n
    
    for time in customers:
        queue[queue.index(min(queue))] += time
    
    return max(queue)

