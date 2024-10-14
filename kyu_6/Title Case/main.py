# Title Case

# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python

def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join(word if word in minor_words else word.capitalize() for word in title)
