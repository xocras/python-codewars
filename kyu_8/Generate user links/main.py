# Generate user links

# https://www.codewars.com/kata/57037ed25a7263ac35000c80/train/python

from urllib.parse import quote

def generate_link(user):
    return f'http://www.codewars.com/users/{quote(user)}'

