# Next bigger number with the same digits

# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

def next_bigger(n):
    # Convert the number to a list of digits
    digits = list(str(n))

    # Find the first digit from the right that is smaller than the digit to its right
    pivot_index = -1
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            pivot_index = i
            break

    # If no such digit is found, return -1 (no bigger number can be formed)
    if pivot_index < 0:
        return pivot_index

    # Find the smallest digit to the right of the pivot index that is greater than the pivot digit
    for i in range(len(digits) - 1, pivot_index, -1):
        if digits[i] > digits[pivot_index]:
            digits[i], digits[pivot_index] = digits[pivot_index], digits[i]
            break

    # Sort the digits to the right of the pivot index in ascending order
    digits[pivot_index + 1:] = sorted(digits[pivot_index + 1:])

    # Convert the list of digits back to an integer and return
    return int(''.join(digits))
