# IP Validation

# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

def is_valid_ip(strng):
    return sum(1 for s in strng.split('.')
               if s.isnumeric()
               and 0 <= int(s) <= 255
               and (len(s) == 1 or s[0] != '0')
               ) == 4
