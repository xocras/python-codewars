# Check the exam

# https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python

def check_exam(arr1,arr2):
    return max(sum(4 if x == y else -1 for x, y in zip(arr1, arr2) if y), 0)
