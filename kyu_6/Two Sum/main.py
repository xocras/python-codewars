# Two Sum

# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

def two_sum(numbers, target):
    hash_table = {}
    
    for i, n in enumerate(numbers):
        difference = target - n
        if difference in hash_table:
            return(hash_table.get(difference), i)
        hash_table[n] = i

